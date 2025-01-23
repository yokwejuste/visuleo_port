import os
from django.core.wsgi import get_wsgi_application
from mangum import Mangum

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "visuleo_port.settings")

application = get_wsgi_application()
handler = Mangum(application)
