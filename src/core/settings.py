"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
import os
from .jazzmin import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)eiunn&!8ui+gth0zadl9&6!5-osnoy_whp3t#l+wh0%i=&oro'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
# "192.168.1.10",
# "192.168.0.109"


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',  # Rest-frameworks default authentication
    'djoser',                    # For Token-based authentication
]


__app_name__ = "page"
__apps__ = BASE_DIR.parent.parent / __app_name__
apps = [
    item
    for item in __import__("os").listdir(
        __apps__.as_posix(),
    )
    if not (item.startswith("_"))
]

for item in apps:

# -----------------------------------------------------------------------------
    # for install apps append
    try:
        INSTALLED_APPS.append(
            # custom modules
            f"{__app_name__}.{item}",
        )
    except Exception:
        print(f"Not found urls in module {item}")

# -----------------------------------------------------------------------------
    # for item in apps:
    url_content = (
        "from django.urls import path\n"
        "from .views import *\n"
        "urlpatterns = []\n"
    )

    url_path = f"src/page/{item}/urls.py"
    try:
        if not os.path.exists(url_path):
            with open(url_path, "w", encoding="utf-8") as file:
                file.write(url_content)
    except Exception as error:
        print(error)
# -----------------------------------------------------------------------------
    # for Serializer fileex

    serializer_content = (
        "from rest_framework import serializers\n"
    )

    serializer_path = f"src/page/{item}/serializers.py"
    try:
        if not os.path.exists(serializer_path):
            with open(serializer_path, "w", encoding="utf-8") as file:
                file.write(serializer_content)
    except Exception as error:
        print(error)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # for model translation
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# SQLite

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'data/Arfa-Med.sqlite3',
    }
}

# PostgreSQL
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Arfa-Medpg',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

PASSWORD_VALIDATION: str = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'{PASSWORD_VALIDATION}.UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{PASSWORD_VALIDATION}.MinimumLengthValidator',
    },
    {
        'NAME': f'{PASSWORD_VALIDATION}.CommonPasswordValidator',
    },
    {
        'NAME': f'{PASSWORD_VALIDATION}.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# Translation -----------------------------------------------------------------

LANGUAGE_CODE = 'en'

USE_TZ = True

USE_L10N = True

USE_I18N = True

TIME_ZONE = 'UTC'

# Specify the languages your application will support
LANGUAGES = [
    ('en', 'English'),
    ('am', 'Armenia'),
    ('ru', 'Russian'),
    # Add more languages as needed
]

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

MODELTRANSLATION_LANGUAGES = ('am', 'ru')
# Set the default language for the site


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = [
    '*',
    # 'http://localhost:3001',
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'Accept',
    'Authorization',
    'Content-Type',
]


JAZZMIN_SETTINGS = JAZZMIN_SETTINGS

JAZZMIN_UI_TWEAKS = JAZZMIN_UI_TWEAKS

# Authentication
# _______________________________________________________________

#
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         # Based-Token Authentication
#         # 'rest_framework.authentication.TokenAuthentication',
#
#         # Session Authentication
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#
#         # SimpleJWT Authentication
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ]
# }

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.parent / f"data/{MEDIA_URL}"





# SIMPLE_JWT = SIMPLE_JWT
