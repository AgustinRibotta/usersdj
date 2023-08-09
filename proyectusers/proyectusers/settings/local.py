from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Data BAse
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret ("DB_NAME"),
        'USER': get_secret ("DB_USER"),
        'PASSWORD': get_secret ("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Direction off JS - IMG - CSS
STATIC_URL = '/static/'
STATIC_DIR = BASE_DIR.child('static')

# Direction off MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# Acceso al correo 
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret("EMAIL")
EMAIL_HOST_PASSWORD =get_secret("EMAIL_PASSWORD")
EMAIL_PORT = 587