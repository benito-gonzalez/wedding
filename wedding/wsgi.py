"""
WSGI config for wedding project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(__file__)
if os.path.isfile(BASE_DIR + '/../.is_development'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding.settings.production')

application = get_wsgi_application()
