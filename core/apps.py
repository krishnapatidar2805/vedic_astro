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
        except Exception:
            pass

