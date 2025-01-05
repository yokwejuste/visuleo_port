from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

from app.visuleo_port.settings.extra import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.environ.get("SECRET_KEY")

# Set DEBUG mode from environment variable
DEBUG = os.environ.get("DEBUG", "True").lower() in ["true", "1"]


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").replace(" ", "").split(",")
INTERNAL_IPS = os.getenv("INTERNAL_IPS", "").split(",")
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")

# Installed Apps
UTILS_APPS = ["debug_toolbar", 'django_extensions']
INSTALLED_APPS = SHARED_APPS + (UTILS_APPS if DEBUG else [])

# Language and Localization
LANGUAGES = (("en", _("English")), ("fr", _("French")), ("de", _("German")))
LOCALE_PATHS = [os.path.join(BASE_DIR, "app/locale")]

# Middleware Configuration
INITIAL_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

MIDDLEWARE = EXTRA_MIDDLEWARE + INITIAL_MIDDLEWARE

if DEBUG:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# URL Configuration
ROOT_URLCONF = "app.visuleo_port.urls"

# Template Configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "app", "templates"),
            os.path.join(BASE_DIR, "app/templates"),
            os.path.join(BASE_DIR, "app", "templates", "pages"),
            os.path.join(BASE_DIR, "app", "templates", "components"),
            os.path.join(BASE_DIR, "app", "templates", "sections"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "django.templatetags.static",
                "slippers.templatetags.slippers",
                "livereload.templatetags.livereload_tags",
            ],
        },
    },
]

# WSGI Configuration
WSGI_APPLICATION = "app.visuleo_port.wsgi.application"

# Database Configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USERNAME"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT", 5432),
    }
}

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Authentication and Sessions
SITE_ID = 1
AUTH_USER_MODEL = "users.VisuleoUser"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Internationalization
LANGUAGE_CODE = "en"
TIME_ZONE = "Africa/Douala"
USE_I18N = True
USE_L10N = True
USE_TZ = True

if not DEBUG:
    # Production S3 Storage Settings
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        },

        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        },
    }

    # AWS Credentials
    AWS_ACCESS_KEY_ID = os.environ.get("S3_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("S3_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.environ.get("S3_REGION_NAME", "us-east-1")
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # URL for serving static and media files
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

    # Define STATIC_ROOT even if using S3 for management commands
    STATIC_ROOT = os.path.join(BASE_DIR, "app", "static")
    MEDIA_ROOT = os.path.join(BASE_DIR, "app", "media")
else:
    # Local Storage Settings for Development
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "app", "staticfiles")]
    STATIC_ROOT = os.path.join(BASE_DIR, "app", "static")
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "app", "media")

    STATICFILES_FINDERS = [
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    ]

# Other Settings
PASSWORD_RESET_TIMEOUT = 14400
MANIFEST_STRICT = False
APPEND_SLASH = True
