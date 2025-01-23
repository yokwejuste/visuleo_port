import os
from django.core.wsgi import get_wsgi_application
from mangum import Mangum

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.visuleo_port.settings.base")

application = get_wsgi_application()
handler = Mangum(application)
