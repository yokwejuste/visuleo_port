import os

# django tenant conf
TENANT_MODEL = "users.Client"
TENANT_DOMAIN_MODEL = "users.Domain"

DATABASE_ROUTERS = ("django_tenants.routers.TenantSyncRouter",)

EXTRA_MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "apps.users.middlewares.django_tenant.TenantMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "apps.users.middlewares.UserTracingMiddleware",
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
    "apps.portfolio",
    "apps.users",
    "django_tenants",
    "oauth2_provider",
    "django_filters",
    "corsheaders",
    "simple_history",
    "allauth",
    "allauth.account",
    "storages",
]

PUBLIC_SCHEMA_URLCONF = "visuleo_port.urls"

SHARED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_browser_reload",
    "django_tenants",
    "allauth.account",
    "oauth2_provider",
    "django_filters",
    "corsheaders",
    "simple_history",
    "allauth",
    "storages",
    "livereload",
    "compressor",
    "passkeys",
    "apps.portfolio",
    "apps.users",
]

# django auth and auth toolkit

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

ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
ROUTE_BASE_VERSION = "v1/"
