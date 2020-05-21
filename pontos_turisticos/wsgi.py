"""
WSGI config for pontos_turisticos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

from dj_static import Cling
from django.core.wsgi import get_wsgi_application
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pontos_turisticos.settings")

application = Cling(get_wsgi_application())
# application = get_wsgi_application()  # Padrao do Django