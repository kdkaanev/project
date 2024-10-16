
import os
from pathlib import Path

from django.urls import reverse_lazy
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY=os.getenv('SECRET_KEY', get_random_secret_key())
DEBUG = bool(int(os.getenv('DEBUG', 0)))
ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(' ')
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_TRUSTED_ORIGINS = ['https://guitar-house.azurewebsites.net']


    
   

   




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "guitar_house.common",
    "guitar_house.accounts",
    "guitar_house.guitar",


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

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
AUTH_USER_MODEL = 'accounts.GuitarHouseUser'

ROOT_URLCONF = 'guitar_house.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'guitar_house.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases



DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD':os.getenv('POSTGRES_PASSWORD'),
            'HOST': os.getenv('POSTGRES_HOST'),
            'PORT': os.getenv('POSTGRES_PORT'),
        }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
else:
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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Directories on the file system

# Directories on the file system
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = BASE_DIR / 'mediafiles'

MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('sign-in')
LOGOUT_REDIRECT_URL = reverse_lazy('index')

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },

    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_USE_TLS = bool(os.getenv('EMAIL_USE_TLS'))  # TLS is required for Gmail SMTP
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER') # Your Gmail email address
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # Your Gmail password or App Password
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587 # or 465 for SSL
EMAIL_USE_TLS=1  # TLS is required for Gmail SMTP
EMAIL_HOST_USER='kaanev8@gmail.com ' # Your Gmail email address
EMAIL_HOST_PASSWORD='zyih ecbn xiye jxnq '  # Your Gmail password or App Password


