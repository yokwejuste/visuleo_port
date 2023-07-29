import uuid
from django.conf import settings
import os


documentation_path = os.path.join(settings.BASE_DIR, "documentation")


def generate_uuid() -> str:
    return str(uuid.uuid4())


def load_document(filename):
    with open(os.path.join(documentation_path, filename)) as f:
        return f.read()
