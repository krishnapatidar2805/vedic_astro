"""
Django settings for Vedic Gajendra Sharma - Astrology Consultation Website
"""

import os
from pathlib import Path
import mimetypes

# Fix for Windows Registry MIME type bug (serving CSS as text/plain)
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("application/javascript", ".js", True)
mimetypes.add_type("text/javascript", ".js", True)

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: change this secret key before deploying to production!
SECRET_KEY = 'django-insecure-CHANGE-THIS-SECRET-KEY-BEFORE-PRODUCTION-vedic-gajendra-sharma'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'http://*.onrender.com',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# ------------------------------------------------------------------
# Application definition
# ------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'core',
    'accounts',
    'services',
    'appointments',
    'blog',
    'gallery',
    'reviews',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vedic_astro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'vedic_astro.wsgi.application'

# ------------------------------------------------------------------
# Database - MySQL
# ------------------------------------------------------------------
# NOTE: To run this project you need `mysqlclient` installed
# (pip install mysqlclient) and a MySQL database created using
# the provided database.sql file.
#
# If you want to quickly test the project without installing MySQL,
# comment the MySQL config below and uncomment the SQLite config.

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('DB_NAME', 'vedic_gajendra_sharma'),
#         'USER': os.environ.get('DB_USER', 'root'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'patidar@'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '3306'),
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     }
# }

# --- Fallback (uncomment to use SQLite instead of MySQL for quick testing) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------------------------------------------------
# Password validation
# ------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------------------------------
# Internationalization
# ------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------------
# Static & Media files
# ------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------------------------------------------
# Auth redirects
# ------------------------------------------------------------------
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'accounts:dashboard'
LOGOUT_REDIRECT_URL = 'core:home'

# ------------------------------------------------------------------
# Email (contact form / notifications) - console backend by default
# ------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'gurmitSharma09@gmail.com'

# ------------------------------------------------------------------
# Business Info (used across templates via context processor)
# ------------------------------------------------------------------
SITE_NAME = 'Vedic Gajendra Sharma'
BUSINESS_PHONE = '+91 7748044076'
BUSINESS_WHATSAPP = '917748044076'
BUSINESS_EMAIL = 'gurmitSharma09@gmail.com'
BUSINESS_INSTAGRAM = 'https://instagram.com/vedic_gajendra_sharma'
BUSINESS_INSTAGRAM_HANDLE = '@vedic_gajendra_sharma'
BUSINESS_ADDRESS = 'Village Kherkheda, Kaleshwar Mandir, Sitamau-Suwasra Road, Tehsil Sitamau, District Mandsaur, Madhya Pradesh'

MESSAGE_TAGS = {
    10: 'debug',
    20: 'info',
    25: 'success',
    30: 'warning',
    40: 'danger',
}
