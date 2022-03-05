import os

from django.core.wsgi import get_wsgi_application

environment = os.environ.get("DJANGO_ENVIRONMENT", "dev")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'settings.{environment}')

application = get_wsgi_application()
