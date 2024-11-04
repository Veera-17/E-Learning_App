from .base import *
DEBUG = False
ADMINS = (
    ('Veera', 'veeratestpress@gmail.com'),
)
ALLOWED_HOSTS = ['.educaproject.com']
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'educa',
       'USER': 'educa',
       'PASSWORD': 'VeeraShree@17',
       'HOST': 'localhost',
        'PORT': '5432',
   }
}

# SSL config
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True