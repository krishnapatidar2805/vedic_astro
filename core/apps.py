import os
import shutil
from django.apps import AppConfig
from django.conf import settings


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        try:
            src = r"C:\Users\Admin\.gemini\antigravity\brain\015abf3c-4c7f-4212-bc3a-ea5a3b956161\.user_uploaded\media_1788072117843.jpg"
            dest = os.path.join(settings.BASE_DIR, 'static', 'img', 'upi_qr.jpg')
            if os.path.exists(src) and not os.path.exists(dest):
                shutil.copyfile(src, dest)
            elif os.path.exists(src):
                shutil.copyfile(src, dest)
            from .models import FAQ
            faqs_data = [
                ('How do I book an astrology appointment?', 'Simply click on "Book Appointment", select your preferred service (e.g. Janam Kundli, Kundli Matching), choose date and time, and submit your details. Pandit ji will confirm your appointment shortly.', 1),
                ('What birth details are required for Kundli Analysis?', 'You need to provide your exact Date of Birth, Time of Birth (AM/PM), and Place of Birth (City/State) for precise astrological and planetary chart calculation.', 2),
                ('Do you provide Online Consultation (Phone & Video Call)?', 'Yes! We offer online consultations worldwide via Phone Call and WhatsApp Video Call, as well as in-person visits at our Mandir location in Sitamau (Mandsaur, MP).', 3),
                ('How can I pay the consultation fees / Dakshina?', 'You can easily pay via UPI, Google Pay, PhonePe, Paytm, or QR Code on our "Pay Online" page, and share the screenshot on WhatsApp (+91 7748044076).', 4),
                ('Is my personal and birth information kept confidential?', '100% Yes. All your personal problems, birth chart data, and consultation details are kept completely private and confidential.', 5),
                ('Can Pandit ji perform Pooja / Katha at our home?', 'Yes, Pandit Gajendra Sharma performs Sangeetmay Shrimad Bhagwat Katha, Kaal Sarp Dosh Shanti, Mangal Bhat Puja, Rudrabhishek, and Vastu Shanti Anushthan at your residence or venue.', 6),
            ]
            for q, a, order in faqs_data:
                FAQ.objects.update_or_create(
                    question=q,
                    defaults={'answer': a, 'order': order, 'is_active': True}
                )
        except Exception:
            pass


