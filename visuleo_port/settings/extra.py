import os

# djanfo tenant conf
TENANT_MODEL = "users.Client"
TENANT_DOMAIN_MODEL = "users.Domain"
DATABASE_ROUTERS = ("django_tenants.routers.TenantSyncRouter",)

TENANT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.portfolio.apps.PortfolioConfig",
    "apps.users.apps.UsersConfig",
    "apps.portfolio.apps.PortfolioConfig",
    "apps.users.apps.UsersConfig",
    "rest_framework",
    "oauth2_provider",
    "drf_yasg",
    "django_filters",
    "corsheaders",
    "simple_history",
    "allauth",
    "allauth.account",
    "storages",
]
DATABASE_ROUTERS = ("django_tenants.routers.TenantSyncRouter",)


PUBLIC_SCHEMA_URLCONF = "visuleo_port.urls_public"

SHARED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.portfolio.apps.PortfolioConfig",
    "apps.users.apps.UsersConfig",
    "django_tenants",
    "rest_framework",
    "oauth2_provider",
    "drf_yasg",
    "django_filters",
    "corsheaders",
    "simple_history",
    "allauth",
    "allauth.account",
    "storages",
]


# swagger configutions
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "basic": {"type": "basic"},
        "oauth2": {
            "type": "oauth2",
            "authorizationUrl": f"{os.environ.get('URL')}/o/authorize/",
            "flow": "implicit",
            "scopes": {
                "read": "Read scope",
                "write": "Write scope",
                "groups": "Access to your groups",
            },
        },
    },
}


# rest framework config
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

# django auth and auth toolkit

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "oauth2_provider.backends.OAuth2Backend",
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
