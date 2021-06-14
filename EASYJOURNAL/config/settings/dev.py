from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [

    # 3rd party apps that aid development
    'django_extensions',

]

# Database Settings for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'easyjournal_db',
        'USER': 'rocksongabriel',
        'PASSWORD': 'iamthedarkbotBORNin1999',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
