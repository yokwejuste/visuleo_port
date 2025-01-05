from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

from app.visuleo_port.settings.extra import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", "True").lower() in ["true", "1"]

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").replace(" ", "").split(",")

INTERNAL_IPS = os.getenv("INTERNAL_IPS", "").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")

UTILS_APPS = [
    "debug_toolbar",
    'django_extensions',
]

INSTALLED_APPS = SHARED_APPS

if DEBUG:
    INSTALLED_APPS += UTILS_APPS


LANGUAGES = (("en", _("English")), ("fr", _("French")))

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "app/locale"),
]

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

MIDDLEWARE = INITIAL_MIDDLEWARE + EXTRA_MIDDLEWARE

if DEBUG:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

ROOT_URLCONF = "app.visuleo_port.urls"

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
                "compressor.templatetags.compress",
                "livereload.templatetags.livereload_tags",
            ],
        },
    },
]

WSGI_APPLICATION = "app.visuleo_port.wsgi.application"

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

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

SITE_ID = 1

AUTH_USER_MODEL = "users.VisuleoUser"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

SESSION_CACHE_ALIAS = "default"

LANGUAGE_CODE = "en"

LANGUAGES = (
    ("fr", _("French")),
    ("en", _("English")),
    ("de", _("German")),
)


TIME_ZONE = "Africa/Douala"

USE_I18N = True

USE_L10N = True

USE_TZ = True

if not DEBUG:
    # AWS Storage Configurations
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    # AWS S3 Credentials
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", "us-east-1")
    AWS_QUERYSTRING_AUTH = False

    # Custom URL for your static/media files
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

else:  # Using local storage for development
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "app", "static")

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "app", "staticfiles"),
    ]

    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "app", "media")


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

PASSWORD_RESET_TIMEOUT = 14400

MANIFEST_STRICT = False

APPEND_SLASH = True
