from .base import *

DEBUG = True

# Database Settings for testing

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
