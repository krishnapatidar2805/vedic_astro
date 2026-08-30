from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FAQ, SiteBanner
from .forms import ContactForm
from services.models import Service
from blog.models import Post
from gallery.models import GalleryImage
from reviews.models import Review
from django.db.models import Avg


def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    posts = Post.objects.filter(status='published')[:3]
    gallery_images = GalleryImage.objects.filter(is_active=True)[:8]
    reviews = Review.objects.filter(is_approved=True)[:6]
    banners = SiteBanner.objects.filter(is_active=True)
    avg_rating = Review.objects.filter(is_approved=True).aggregate(Avg('rating'))['rating__avg'] or 5
    context = {
        'services': services,
        'posts': posts,
        'gallery_images': gallery_images,
        'reviews': reviews,
        'banners': banners,
        'avg_rating': round(avg_rating, 1),
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for reaching out! We will get back to you soon.')
            return redirect('core:contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def faq(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'core/faq.html', {'faqs': faqs})


def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')


def payment(request):
    return render(request, 'core/payment.html')


def festivals(request):
    festivals_list = [
        {
            'name': 'Maha Shivratri (महाशिवरात्रि)',
            'category': 'shivratri',
            'tithi': 'Phalguna Krishna Chaturdashi',
            'date': 'Auspicious Annual Shivaratri',
            'significance': 'Lord Shiva and Goddess Parvati divine marriage celebration. Removes planetary malefic effects and bestows peace, health, and longevity.',
            'mantra': 'ॐ नमः शिवाय (Om Namah Shivaya)',
            'vidhi': 'Rudrabhishek with Panchamrit, Belpatra, Dhatura, and overnight Jagran with Mahamrityunjaya Japa.',
            'badge': 'Major Festival',
            'icon': 'fa-solid fa-om'
        },
        {
            'name': 'Shardiya Navratri (शारदीय नवरात्रि)',
            'category': 'festivals',
            'tithi': 'Ashwina Shukla Pratipada to Navami',
            'date': '9 Divine Nights of Goddess Durga',
            'significance': 'Celebration of Shakti, victory of good over evil. Removes all obstacles, enemies, and Rahu-Ketu doshas.',
            'mantra': 'ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे',
            'vidhi': 'Ghatasthapana, Durga Saptashati Path, Kanya Pujan, and Hawan Anushthan.',
            'badge': 'Navratri Anushthan',
            'icon': 'fa-solid fa-sun'
        },
        {
            'name': 'Shri Krishna Janmashtami (श्रीकृष्ण जन्माष्टमी)',
            'category': 'festivals',
            'tithi': 'Bhadrapada Krishna Ashtami',
            'date': 'Midnight Rohini Nakshatra',
            'significance': 'Birth celebration of Lord Krishna. Bestows happiness in progeny (Santan Sukh), peace in marriage, and spiritual awakening.',
            'mantra': 'ॐ नमो भगवते वासुदेवाय (Om Namo Bhagavate Vasudevaya)',
            'vidhi': 'Ladoo Gopal Abhishek with milk, honey, Makhan Bhog, and midnight Aarti.',
            'badge': 'Shri Krishna Puja',
            'icon': 'fa-solid fa-feather'
        },
        {
            'name': 'Deepawali & Dhanteras (दीपावली एवं धनतेरस)',
            'category': 'festivals',
            'tithi': 'Kartika Krishna Trayodashi to Amavasya',
            'date': '5 Days of Light & Prosperity',
            'significance': 'Maha Lakshmi, Lord Kuber, and Lord Ganesha worship for wealth, business expansion, and debt relief.',
            'mantra': 'ॐ श्रीं ह्रीं क्लीं त्रिभुवन महालक्ष्म्यै अस्मांक दारिद्र्य नाशय प्रचुर धन देहि देहि क्लीं ह्रीं श्रीं ॐ',
            'vidhi': 'Lakshmi-Kuber Pujan, Shri Suktam Path, Deepak Sthapana in auspicious Sthir Lagna.',
            'badge': 'Lakshmi Kuber Puja',
            'icon': 'fa-solid fa-fire'
        },
        {
            'name': 'Nirjala Ekadashi (निर्जला एकादशी)',
            'category': 'ekadashi',
            'tithi': 'Jyeshtha Shukla Ekadashi',
            'date': 'Most Sacred Ekadashi Vrat',
            'significance': 'Observing this single fast provides the sacred merit (punya) of all 24 Ekadashis combined. Removes severe sins and brings salvation.',
            'mantra': 'ॐ नमो नारायणाय (Om Namo Narayanaya)',
            'vidhi': 'Waterless fasting, Vishnu Sahasranama chanting, donation of water pots, umbrellas, and food to Brahmins.',
            'badge': 'Maha Ekadashi',
            'icon': 'fa-solid fa-star'
        },
        {
            'name': 'Devshayani Ekadashi (देवशयनी एकादशी)',
            'category': 'ekadashi',
            'tithi': 'Ashadha Shukla Ekadashi',
            'date': 'Start of Chaturmas',
            'significance': 'Lord Vishnu enters Yoga Nidra for four sacred months. Ideal for spiritual vows, Bhagwat Katha, and holy anushthans.',
            'mantra': 'सुप्ते त्वयि जगन्नाथ जगत् सुप्तं भवेदिदम्। विबुद्धे त्वयि बुध्येत सर्वं विश्वं सचराचरम्॥',
            'vidhi': 'Tulsi worship, Sattvic fasting, and initiation of Chaturmas Anushthan.',
            'badge': 'Chaturmas Start',
            'icon': 'fa-solid fa-moon'
        },
        {
            'name': 'Pradosh Vrat (प्रदोष व्रत - सोम, शनि व भौम)',
            'category': 'pradosh',
            'tithi': 'Trayodashi Tithi (Both Waxing & Waning)',
            'date': 'Twice Every Month at Twilight',
            'significance': 'Dedicated to Lord Shiva during Pradosh Kaal (sunset). Som Pradosh removes mental stress; Shani Pradosh cures Sade Sati; Bhauma Pradosh removes debts (Rin Mukti).',
            'mantra': 'ॐ तत्पुरुषाय विद्महे महादेवाय धीमहि तन्नो रुद्रः प्रचोदयात्॥',
            'vidhi': 'Evening Shiva Puja during sunset, Bilvapatra archana, and Shiva Chalisa recital.',
            'badge': 'Dosh Nivaran Vrat',
            'icon': 'fa-solid fa-bell'
        },
        {
            'name': 'Sharad Purnima (शरद पूर्णिमा - कोजागरी)',
            'category': 'purnima',
            'tithi': 'Ashwina Shukla Purnima',
            'date': 'Amrit Varsha Full Moon',
            'significance': 'Moon rays shower divine nectar (Amrit). Blesses with health, youthfulness, and fulfillment of material desires.',
            'mantra': 'ॐ सोमाय नमः (Om Somaya Namah)',
            'vidhi': 'Placing Kheer under moonlight overnight, Satyanarayan Vrat Katha, and Chandra Arghya.',
            'badge': 'Amrit Purnima',
            'icon': 'fa-solid fa-moon'
        },
        {
            'name': 'Somvati Amavasya (सोमवती अमावस्या)',
            'category': 'purnima',
            'tithi': 'Amavasya falling on Monday',
            'date': 'Pitra Tarpan & Dosh Shanti',
            'significance': 'Extremely powerful day for Pitra Dosh Shanti, Kaal Sarp Dosh nivaran, and longevity of husband (Akhand Saubhagya).',
            'mantra': 'ॐ पितृभ्यः स्वधायिभ्यः स्वधा नमः',
            'vidhi': 'Peepal tree 108 parikrama, Pitra Tarpan, feeding cows, and Shanti Pujan.',
            'badge': 'Pitra Dosh Shanti',
            'icon': 'fa-solid fa-hands-praying'
        },
        {
            'name': 'Shri Ganesh Chaturthi (श्री गणेश चतुर्थी)',
            'category': 'festivals',
            'tithi': 'Bhadrapada Shukla Chaturthi',
            'date': '10 Days of Ganeshotsav',
            'significance': 'Invocation of Lord Ganesha to remove obstacles (Vighnaharta), bestow wisdom (Buddhi), and prosperity (Riddhi-Siddhi).',
            'mantra': 'ॐ गं गणपतये नमः (Om Gam Ganapataye Namah)',
            'vidhi': 'Sthapana of Clay Ganesha idol, 21 Durva grass offerings, Modak Bhog, and Atharvashirsha path.',
            'badge': 'Riddhi Siddhi Puja',
            'icon': 'fa-solid fa-spa'
        },
        {
            'name': 'Makar Sankranti (मकर संक्रांति)',
            'category': 'festivals',
            'tithi': 'Surya enters Capricorn (Makara Rashi)',
            'date': 'Auspicious Surya Uttarayan',
            'significance': 'Surya Deva transitions into Makara Rashi. Sacred day for Sun worship, removing Pitra Dosh, and increasing self-confidence and health.',
            'mantra': 'ॐ सूर्याय नमः (Om Suryaya Namah)',
            'vidhi': 'Holy river dip, Surya Arghya with copper pot, and donation of sesame (Til) and jaggery (Gud).',
            'badge': 'Surya Aradhana',
            'icon': 'fa-solid fa-sun'
        },
        {
            'name': 'Guru Purnima (गुरु पूर्णिमा - व्यास पूर्णिमा)',
            'category': 'purnima',
            'tithi': 'Ashadha Shukla Purnima',
            'date': 'Sacred Day of the Spiritual Guru',
            'significance': 'Honoring Vedic Gurus, Maharshi Ved Vyasa, and receiving spiritual blessings for knowledge and intellect.',
            'mantra': 'गुरुर्ब्रह्मा गुरुर्विष्णुः गुरुर्देवो महेश्वरः। गुरुः साक्षात् परं ब्रह्म तस्मै श्रीगुरवे नमः॥',
            'vidhi': 'Guru Paduka Pujan, Guru Mantra Japa, offering yellow clothes and fruits to Vedic scholars and spiritual masters.',
            'badge': 'Guru Vandana',
            'icon': 'fa-solid fa-book-open'
        }
    ]
    return render(request, 'core/festivals.html', {'festivals': festivals_list})


def terms_conditions(request):
    return render(request, 'core/terms_conditions.html')


def search(request):
    query = request.GET.get('q', '')
    services = Service.objects.filter(is_active=True, title__icontains=query) if query else Service.objects.none()
    posts = Post.objects.filter(status='published', title__icontains=query) if query else Post.objects.none()
    return render(request, 'core/search_results.html', {'query': query, 'services': services, 'posts': posts})


def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)
