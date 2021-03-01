"""
Django settings for techup project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7pgm!f062)+wellq8no=#kq2&=x+_^07i3cs0=qh1vd&s%$123'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PRODUCTION = False

ALLOWED_HOSTS = ["192.168.10.5"]


# Application definition

INSTALLED_APPS = [
    'designs',
    'dashboard',    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'escapejson',
    'crispy_forms'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# AUTHENTICATION_BACKENDS = [
#     'techup.backends.AuthBackend'
# ]

ROOT_URLCONF = 'techup.urls'

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
            'libraries':{
                'tag_custom': 'dashboard.templatetags.tag_custom',
            }
        },
    },
]

WSGI_APPLICATION = 'techup.wsgi.application'
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# RDS_USERNAME = ""
# RDS_PASSWORD = "D1WSyQKbeZZk7WBR"

if 'RDS_HOSTNAME' in os.environ:
    ALLOWED_HOSTS = ["tech.us-east-2.elasticbeanstalk.com", "jumpcut.online"]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
    PRODUCTION = True
    DEBUG = bool(os.environ.get('debug'))
else:
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data.db'),
        }
    }

# AUTH_USER_MODEL = ''

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

#AUTH_PASSWORD_VALIDATORS = [
#    {
#        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#    },
#]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

if "AWS_ACCESS_KEY_ID" in os.environ and "AWS_STORAGE_BUCKET_NAME" in os.environ:
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
    AWS_DEFAULT_ACL = None
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_REGION_NAME = "us-east-2"
    AWS_S3_ENCRYPTION = True
    AWS_S3_HOST = ''
    AWS_IS_GZIPPED = True
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL=os.environ.get('STATIC_URL', default=f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com')
else:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

SITE_URL="https://"
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SENDGRID_API_KEY=os.environ.get('SENDGRID_API_KEY')
RESET_EMAIL_TEMPLATE_ID=''
#EMAIL_HOST = "email-smtp.us-west-2.amazonaws.com"
EMAIL_PORT = 587
#EMAIL_HOST_USER = "AKIAU6V5ERXY5WHDA4FP"
#EMAIL_HOST_PASSWORD = "BLn8mRInor8m4kAx+86Znvb7Krb0gOpmqfUBJ4pFcqm5"
EMAIL_FROM = "hello@hello.io"
NAME_FROM = "Hello"
EMAIL_USE_TLS = True
MAX_UPLOAD_SIZE = 5242880

STRIPE_PUBLISHABLE_KEY = 'pk_test_51IOctcK38c4gnA4gHppkpRZr8C6fANplKeK5G1HpSNzx3nypkGTX3BDReGHMdYCPOY6OzhQBKKzBFzG05DXHLh7o00wqxVDPmy'
STRIPE_SECRET_KEY = 'sk_test_51IOctcK38c4gnA4g58HhgJmkZqHUxdX3OzwntMw5vDFTl4X5MGGLv6cFaIEMwK0V3XB2VnWAMtco5jW6RPFLJYkr00PsUy5qzm'
STRIPE_ENDPOINT_SECRET = ''