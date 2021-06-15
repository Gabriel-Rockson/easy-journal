import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EASYJOURNAL.settings') # TODO to be changed in prod settings

application = get_wsgi_application()
