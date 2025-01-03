import os

TENANT_MODEL = "users.Client"
TENANT_DOMAIN_MODEL = "users.Domain"

DATABASE_ROUTERS = ("django_tenants.routers.TenantSyncRouter",)

EXTRA_MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'allauth.account.middleware.AccountMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "app.dj_apps.users.middlewares.django_tenant.TenantMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "app.dj_apps.users.middlewares.UserTracingMiddleware",
    "django_tenants.middleware.main.TenantMainMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "livereload.middleware.LiveReloadScript",
]

TENANT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app.dj_apps.portfolio",
    "app.dj_apps.users",
    "oauth2_provider",
    "django_filters",
    "corsheaders",
    "simple_history",
    "storages",
    "allauth_ui",
    "allauth",
]

PUBLIC_SCHEMA_URLCONF = "app.visuleo_port.urls"

SHARED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_browser_reload",
    "django_tenants",
    "compressor",
    "oauth2_provider",
    "django_filters",
    "corsheaders",
    "simple_history",
    "allauth_ui",
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
    "oauth2_provider.backends.OAuth2Backend",
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
