import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oh_so_like_it.settings')

application = get_asgi_application()
