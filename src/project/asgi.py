import os

from django.core.asgi import get_asgi_application

environment = os.environ.get("DJANGO_ENVIRONMENT", "dev")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'settings.{environment}')

application = get_asgi_application()
