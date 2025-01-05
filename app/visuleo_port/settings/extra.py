import os

from django.templatetags.static import static


EXTRA_MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'allauth.account.middleware.AccountMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "app.dj_apps.users.middlewares.UserTracingMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "livereload.middleware.LiveReloadScript",
]

PUBLIC_SCHEMA_URLCONF = "app.visuleo_port.urls"

SHARED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_browser_reload",
    "django_filters",
    "corsheaders",
    "simple_history",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.google",
    "widget_tweaks",
    "storages",
    'slippers',
    "livereload",
    "passkeys",
    "app.dj_apps.portfolio",
    "app.dj_apps.users",
]

AUTHENTICATION_BACKENDS = [
    "passkeys.backend.PasskeyModelBackend",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

OAUTH2_PROVIDER = {
    "ACCESS_TOKEN_EXPIRE_SECONDS": 60 * 60,
    "REFRESH_TOKEN_EXPIRE_SECONDS": 60 * 60 * 24 * 30,
    "ROTATE_REFRESH_TOKENS": True,
    "ALLOWED_REDIRECT_URI_SCHEMES": ["http", "https", "localhost"],
    "SCOPES": {
        "read": "Read scope",
        "write": "Write scope",
        "groups": "Access to your groups",
    },
}

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
ROUTE_BASE_VERSION = "v1/"

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = os.getenv('CELERY_ACCEPT_CONTENT', 'json').split(',')
CELERY_TASK_SERIALIZER = os.getenv('CELERY_TASK_SERIALIZER', 'json')
CELERY_RESULT_SERIALIZER = os.getenv('CELERY_RESULT_SERIALIZER', 'json')
CELERY_TIMEZONE = os.getenv('CELERY_TIMEZONE', 'UTC')
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True


# # Django Unfold Admin Setting
UNFOLD = {
    "SHOW_LANGUAGES": True,
    "SITE_ICON": {
        "light": lambda request: static("images/logo/logo.svg"),
        "dark": lambda request: static("images/logo/logo-white.svg"),
    },
    "SITE_LOGO": {
        "light": lambda request: static("images/logo/logo.svg"),
        "dark": lambda request: static("images/logo/logo-white.svg"),
    },
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "LOGIN": {
        "image": lambda request: static("images/login_side.svg"),
    },
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "229 246 240",
            "100": "205 237 226",
            "200": "178 228 211",
            "300": "150 218 196",
            "400": "117 203 178",
            "500": "89 192 156",
            "600": "70 164 124",
            "700": "54 131 99",
            "800": "47 111 84",
            "900": "36 83 63",
            "950": "28 58 43"
        }
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
}
