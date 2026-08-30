from django.conf import settings
import urllib.parse


def site_settings(request):
    """Make business info available in every template."""
    whatsapp_number = settings.BUSINESS_WHATSAPP
    default_msg = "Hello Pandit ji, I would like to consult with you for Vedic Astrology services."
    encoded_msg = urllib.parse.quote(default_msg)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_msg}"

    return {
        'SITE_NAME': settings.SITE_NAME,
        'BUSINESS_PHONE': settings.BUSINESS_PHONE,
        'BUSINESS_WHATSAPP': whatsapp_number,
        'BUSINESS_WHATSAPP_URL': whatsapp_url,
        'BUSINESS_EMAIL': settings.BUSINESS_EMAIL,
        'BUSINESS_INSTAGRAM': settings.BUSINESS_INSTAGRAM,
        'BUSINESS_INSTAGRAM_HANDLE': getattr(settings, 'BUSINESS_INSTAGRAM_HANDLE', '@vedic_gajendra_sharma'),
        'BUSINESS_ADDRESS': settings.BUSINESS_ADDRESS,
    }
