from django.core.exceptions import ImproperlyConfigured
import json
from pathlib import Path
from unipath import Path

# Calling the secret.json file
with open('secret.json') as f:
    secret = json.loads(f.read())
    
def get_secret(secret_name, secrets = secret):
    try:
        return secrets[secret_name]
    except:
        msg = 'La variable %s no existe' % secret_name
        raise ImproperlyConfigured(msg)

BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = get_secret ("SECRET_KEY")

# Django Apps
DJANGO_APPS =  (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Local Apps
LOCAL_APPS = (
    'applications.home',
    'applications.users',
)

# Third Party Apps
THIRD_PARTY_APPS = ()

# Aplicaciones
INSTALLED_APPS = ( DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyectusers.urls'

# Template route
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR.child('template') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyectusers.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Indicamos donde esta el nuevo modelo de user
AUTH_USER_MODEL = 'users.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

