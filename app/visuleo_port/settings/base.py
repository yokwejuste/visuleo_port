from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

from app.visuleo_port.settings.extra import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", "False").lower() in ["true", "1"]

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").replace(" ", "").split(",")

INTERNAL_IPS = os.getenv("INTERNAL_IPS", "").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")

UTILS_APPS = [
    "debug_toolbar",
    'django_extensions',
]

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

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
        "ENGINE": "django_tenants.postgresql_backend",
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

TIME_ZONE = "Africa/Douala"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "app", "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "app", "staticfiles"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "app", "media")

COMPRESS_ROOT = STATIC_ROOT

COMPRESS_ENABLED = os.environ.get("COMPRESS_ENABLED", "False").lower() in ["true", "1"]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    'compressor.finders.CompressorFinder',
]

PASSWORD_RESET_TIMEOUT = 14400

MANIFEST_STRICT = False

APPEND_SLASH = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'error.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
