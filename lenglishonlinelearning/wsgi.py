"""
WSGI config for lenglishonlinelearning project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lenglishonlinelearning.settings")

application = get_wsgi_application()
