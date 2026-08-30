from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'

    def ready(self):
        try:
            from .models import Service
            
            services_data = [
                ('Kaal Sarp Dosh Shanti Puja', 'kaal-sarp-dosh-puja', 'fa-solid fa-fire', 
                 'Vedic rituals and anushthan for complete Kaal Sarp Dosh Nivaran.', 
                 'Authentic Kaal Sarp Dosh Shanti Puja performed according to Vedic scriptures with complete mantras, havan, and anushthan to remove obstacles, bring peace, prosperity, and spiritual growth.', 3100.0, 1),
                
                ('Mangal Bhat Puja', 'mangal-puja', 'fa-solid fa-fire', 
                 'Sacred Mangal Bhat Puja & Manglik Dosh Shanti Anushthan.', 
                 'Special Vedic Mangal Bhat Puja and Manglik Dosh Nivaran Vidhi performed to resolve marriage delays, relationship harmony, career obstacles, and planetary afflictions of Mars.', 3100.0, 2),
                
                ('Janam Kundli Analysis', 'janam-kundli-analysis', 'fa-solid fa-moon', 
                 'Detailed birth chart reading to understand your life path.', 
                 'A complete Janam Kundli (birth chart) analysis based on your exact date, time, and place of birth. Understand planetary positions, doshas, and remedies for a balanced life.', 501.0, 3),
                
                ('Kundli Matching', 'kundli-matching', 'fa-solid fa-heart', 
                 'Guna Milan for marriage compatibility between partners.', 
                 'Traditional Ashtakoot Guna Milan matching to assess compatibility between prospective partners before marriage, including Manglik Dosh analysis.', 501.0, 4),
                
                ('Marriage Problem Solution', 'marriage-problem-solution', 'fa-solid fa-ring', 
                 'Astrological remedies for delays and conflicts in marriage.', 
                 'Personalized remedies and pujas to resolve marriage delays, conflicts, and compatibility issues rooted in Vedic astrology.', 701.0, 5),
                
                ('Career & Business Guidance', 'career-and-business-guidance', 'fa-solid fa-briefcase', 
                 'Astrological direction for career growth and business success.', 
                 'Guidance on career choices, job changes, business partnerships, and financial growth based on planetary influences in your chart.', 601.0, 6),
                
                ('Vastu Shanti', 'vastu-shanti', 'fa-solid fa-house', 
                 'Vastu correction for home and office harmony.', 
                 'Complete Vastu Shastra consultation and remedies for your home or office to bring positive energy, health, and prosperity.', 0.0, 7),
                
                ('Numerology Reading', 'numerology-reading', 'fa-solid fa-hashtag', 
                 'Discover the power of numbers in your life.', 
                 'Numerology analysis based on your name and date of birth to guide important life decisions.', 401.0, 8),
                
                ('Grah Dosh Nivaran', 'grah-dosh-nivaran', 'fa-solid fa-fire', 
                 'Remedies for malefic planetary doshas.', 
                 'Identification and remedy of Grah Dosh, Kaal Sarp Dosh, Sade Sati and other planetary afflictions through pujas and mantras.', 801.0, 9),
                
                ('Palmistry (Hast Rekha)', 'palmistry-hast-rekha', 'fa-solid fa-hand', 
                 'Read your destiny through the lines of your palm.', 
                 'Traditional palmistry reading to reveal insights about your health, career, relationships, and future.', 301.0, 10),
                
                ('Muhurat Selection', 'muhurat-selection', 'fa-solid fa-clock', 
                 'Auspicious timing for weddings, griha pravesh & more.', 
                 'Selection of the most auspicious Muhurat for weddings, Griha Pravesh, business launch, and other important life events.', 501.0, 11),
                
                ('Court Case Problem', 'court-case-problem', 'fa-solid fa-scale-balanced', 
                 'Astrological remedies to support favorable legal outcomes.', 
                 'Vedic remedies and puja recommendations to strengthen your position in ongoing legal and court matters.', 701.0, 12),
                
                ('Financial Problem Solution', 'financial-problem-solution', 'fa-solid fa-chart-line', 
                 'Remedies to overcome financial struggles and debt.', 
                 'Astrological analysis and remedies aimed at resolving financial difficulties, debts, and attracting prosperity.', 601.0, 13),
                
                ('Shrimad Bhagwat Katha', 'shrimad-bhagwat-katha', 'fa-solid fa-om', 
                 'Sacred musical Bhagwat Katha recitation for your family.', 
                 'Sangeetmay Shrimad Bhagwat Katha along with Yagna, Rudrabhishek, Durga Saptashati Path and other Vedic Anushthans performed at your home.', 0.0, 14),
            ]

            for title, slug, icon, short_desc, desc, price, order in services_data:
                Service.objects.update_or_create(
                    slug=slug,
                    defaults={
                        'title': title,
                        'short_description': short_desc,
                        'description': desc,
                        'icon': icon,
                        'price': price,
                        'is_active': True,
                        'order': order,
                    }
                )
        except Exception:
            pass
