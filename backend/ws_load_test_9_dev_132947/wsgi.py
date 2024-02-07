"""
WSGI config for ws_load_test_9_dev_132947 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "ws_load_test_9_dev_132947.settings"
)

application = get_wsgi_application()
