from django.core.management.base import BaseCommand
from django.core.files import File
from django.contrib.auth.models import User
from services.models import Service
from core.models import FAQ
from gallery.models import GalleryImage, GalleryCategory
from blog.models import Post, Category
from reviews.models import Review
import os


class Command(BaseCommand):
    help = 'Seed the database with sample demo data for Vedic Gajendra Sharma website'

    def handle(self, *args, **options):
        base = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'static', 'img')

        # ---- Services ----
        services_data = [
            ('Kaal Sarp Dosh Shanti Puja', 'fa-solid fa-fire', 'Vedic rituals and anushthan for complete Kaal Sarp Dosh Nivaran.', 'Authentic Kaal Sarp Dosh Shanti Puja performed according to Vedic scriptures with complete mantras, havan, and anushthan to remove obstacles, bring peace, prosperity, and spiritual growth.', 3100),
            ('Mangal Bhat Puja', 'fa-solid fa-fire', 'Sacred Mangal Bhat Puja & Manglik Dosh Shanti Anushthan.', 'Special Vedic Mangal Bhat Puja and Manglik Dosh Nivaran Vidhi performed to resolve marriage delays, relationship harmony, career obstacles, and planetary afflictions of Mars.', 3100),
            ('Janam Kundli Analysis', 'fa-solid fa-moon', 'Detailed birth chart reading to understand your life path.', 'A complete Janam Kundli (birth chart) analysis based on your exact date, time, and place of birth. Understand planetary positions, doshas, and remedies for a balanced life.', 501),
            ('Kundli Matching', 'fa-solid fa-heart', 'Guna Milan for marriage compatibility between partners.', 'Traditional Ashtakoot Guna Milan matching to assess compatibility between prospective partners before marriage, including Manglik Dosh analysis.', 501),
            ('Marriage Problem Solution', 'fa-solid fa-ring', 'Astrological remedies for delays and conflicts in marriage.', 'Personalized remedies and pujas to resolve marriage delays, conflicts, and compatibility issues rooted in Vedic astrology.', 701),
            ('Career & Business Guidance', 'fa-solid fa-briefcase', 'Astrological direction for career growth and business success.', 'Guidance on career choices, job changes, business partnerships, and financial growth based on planetary influences in your chart.', 601),
            ('Vastu Shanti', 'fa-solid fa-house', 'Vastu correction for home and office harmony.', 'Complete Vastu Shastra consultation and remedies for your home or office to bring positive energy, health, and prosperity.', 0),
            ('Numerology Reading', 'fa-solid fa-hashtag', 'Discover the power of numbers in your life.', 'Numerology analysis based on your name and date of birth to guide important life decisions.', 401),
            ('Grah Dosh Nivaran', 'fa-solid fa-fire', 'Remedies for malefic planetary doshas.', 'Identification and remedy of Grah Dosh, Kaal Sarp Dosh, Sade Sati and other planetary afflictions through pujas and mantras.', 801),
            ('Palmistry (Hast Rekha)', 'fa-solid fa-hand', 'Read your destiny through the lines of your palm.', 'Traditional palmistry reading to reveal insights about your health, career, relationships, and future.', 301),
            ('Muhurat Selection', 'fa-solid fa-clock', 'Auspicious timing for weddings, griha pravesh & more.', 'Selection of the most auspicious Muhurat for weddings, Griha Pravesh, business launch, and other important life events.', 501),
            ('Court Case Problem', 'fa-solid fa-scale-balanced', 'Astrological remedies to support favorable legal outcomes.', 'Vedic remedies and puja recommendations to strengthen your position in ongoing legal and court matters.', 701),
            ('Financial Problem Solution', 'fa-solid fa-chart-line', 'Remedies to overcome financial struggles and debt.', 'Astrological analysis and remedies aimed at resolving financial difficulties, debts, and attracting prosperity.', 601),
            ('Shrimad Bhagwat Katha', 'fa-solid fa-om', 'Sacred musical Bhagwat Katha recitation for your family.', 'Sangeetmay Shrimad Bhagwat Katha along with Yagna, Rudrabhishek, Durga Saptashati Path and other Vedic Anushthans performed at your home.', 0),
        ]
        for title, icon, short_desc, desc, price in services_data:
            slug = title.lower().replace(' ', '-').replace('&', 'and').replace('(', '').replace(')', '')
            Service.objects.get_or_create(
                slug=slug,
                defaults=dict(title=title, icon=icon, short_description=short_desc, description=desc, price=price, is_active=True)
            )
        self.stdout.write(self.style.SUCCESS(f'Created {Service.objects.count()} services'))

        # ---- FAQs ----
        faqs_data = [
            ('How do I book an appointment?', 'Simply register on our website, go to the "Book Appointment" page, select your preferred service, date and time, and submit the form. We will contact you to confirm.'),
            ('What details do I need to provide for Kundli analysis?', 'You need to provide your accurate date of birth, time of birth, and place of birth for a precise Janam Kundli analysis.'),
            ('Do you offer online consultations?', 'Yes, we offer consultations via phone call and WhatsApp video call in addition to in-person visits.'),
            ('Is my personal information kept confidential?', 'Absolutely. All your personal and birth details are kept strictly confidential and used only for your consultation.'),
            ('What are your consultation charges?', 'Charges vary by service type. Please check individual service pages or contact us directly for current pricing.'),
        ]
        for q, a in faqs_data:
            FAQ.objects.get_or_create(question=q, defaults={'answer': a})
        self.stdout.write(self.style.SUCCESS(f'Created {FAQ.objects.count()} FAQs'))

        # ---- Gallery ----
        cat, _ = GalleryCategory.objects.get_or_create(name='Posters & Services')
        poster_files = ['poster1.jpeg', 'poster2.jpeg', 'poster3.jpeg', 'poster4.jpeg']
        poster_titles = ['Astrology Services', 'Sangeetmay Shrimad Bhagwat Katha', 'Vedic Pujan & Astrology', 'Contact for Vedic Poojan']
        for fname, title in zip(poster_files, poster_titles):
            fpath = os.path.join(base, fname)
            if os.path.exists(fpath) and not GalleryImage.objects.filter(title=title).exists():
                with open(fpath, 'rb') as f:
                    gi = GalleryImage(title=title, category=cat, is_active=True)
                    gi.image.save(fname, File(f), save=True)
        self.stdout.write(self.style.SUCCESS(f'Created {GalleryImage.objects.count()} gallery images'))

        # ---- Blog ----
        bcat, _ = Category.objects.get_or_create(name='Astrology Tips', slug='astrology-tips')
        admin_user = User.objects.filter(is_superuser=True).first()
        posts_data = [
            ('Understanding Your Janam Kundli', 'janam-kundli-guide', 'Learn the basics of reading your birth chart and what it reveals about your life.', 'Your Janam Kundli is a map of the sky at the exact moment of your birth. It reveals the positions of the nine planets (Navagraha) across the twelve houses, forming the foundation for all astrological predictions...\n\nUnderstanding your Kundli helps identify strengths, challenges, and the right remedies for a balanced and prosperous life.'),
            ('5 Signs You Need Vastu Correction', 'vastu-correction-signs', 'Common signs in your home or office that indicate the need for Vastu Shanti.', 'Frequent health issues, financial instability, family conflicts, and lack of sleep can sometimes be linked to Vastu Dosh in your home or workplace...\n\nA proper Vastu consultation can identify these imbalances and suggest simple corrections to restore harmony.'),
            ('Importance of Kundli Matching Before Marriage', 'kundli-matching-importance', 'Why Guna Milan remains a trusted tradition for compatible marriages.', 'Kundli Matching, or Guna Milan, examines 36 Gunas (attributes) between two individuals to assess compatibility in areas of health, wealth, and temperament...\n\nThis ancient practice continues to guide families toward harmonious and lasting marriages.'),
        ]
        for title, slug, summary, content in posts_data:
            Post.objects.get_or_create(slug=slug, defaults=dict(
                title=title, author=admin_user, category=bcat, summary=summary, content=content, status='published'
            ))
        self.stdout.write(self.style.SUCCESS(f'Created {Post.objects.count()} blog posts'))

        self.stdout.write(self.style.SUCCESS('Seeding complete! You can now log in to /admin/ with your superuser account.'))
