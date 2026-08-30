from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'

    def ready(self):
        try:
            from .models import Service
            # 1. Update Vastu Shanti price to 0 (hide price display)
            Service.objects.filter(slug='vastu-shanti').update(price=0)

            # 2. Add or update Kaal Sarp Dosh Shanti Puja (Price: 3100)
            Service.objects.update_or_create(
                slug='kaal-sarp-dosh-puja',
                defaults={
                    'title': 'Kaal Sarp Dosh Shanti Puja',
                    'short_description': 'Vedic rituals and anushthan for complete Kaal Sarp Dosh Nivaran.',
                    'description': 'Authentic Kaal Sarp Dosh Shanti Puja performed according to Vedic scriptures with complete mantras, havan, and anushthan to remove obstacles, bring peace, prosperity, and spiritual growth.',
                    'icon': 'fa-solid fa-fire',
                    'price': 3100.0,
                    'is_active': True,
                    'order': 1,
                }
            )

            # 3. Add or update Mangal Bhat Puja (Price: 3100)
            Service.objects.update_or_create(
                slug='mangal-puja',
                defaults={
                    'title': 'Mangal Bhat Puja',
                    'short_description': 'Sacred Mangal Bhat Puja & Manglik Dosh Shanti Anushthan.',
                    'description': 'Special Vedic Mangal Bhat Puja and Manglik Dosh Nivaran Vidhi performed to resolve marriage delays, relationship harmony, career obstacles, and planetary afflictions of Mars.',
                    'icon': 'fa-solid fa-fire',
                    'price': 3100.0,
                    'is_active': True,
                    'order': 2,
                }
            )
        except Exception:
            pass

