from .base import *

DEBUG = False

# Database Settings for production

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
