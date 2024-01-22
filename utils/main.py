import os
import uuid

documentation_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "documentation/")


def generate_uuid() -> str:
    return str(uuid.uuid4())


def load_documentation(filename) -> str:
    with open(os.path.join(documentation_path, filename), "r") as doc:
        return doc.read()
