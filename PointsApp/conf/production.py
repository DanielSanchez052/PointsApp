from PointsApp.conf.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True, cast=bool)


ALLOWED_HOSTS = ['0.0.0.0','localhost', 'localhost:85', '127.0.0.1', env('SERVER', default='127.0.0.1')]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'',
        'USER':env('DB_USER'),
        'PASSWORD':env('DB_PASS'),
        'HOST':'',
        'PORT':''
    }
}
