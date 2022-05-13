import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oh_so_like_it.settings')

application = get_wsgi_application()
