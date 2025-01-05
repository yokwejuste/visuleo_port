from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.dj_apps.users.views.index import visu_404

ROUTE_BASE_VERSION = settings.ROUTE_BASE_VERSION


if settings.DEBUG:
    urlpatterns = (
            [
                path("__debug__/", include("debug_toolbar.urls")),
                path("__reload__/", include("django_browser_reload.urls")),
                path("i18n/", include("django.conf.urls.i18n")),
            ] + i18n_patterns(
                path('accounts/', include('allauth.urls')),
        path('', include(
            ("app.dj_apps.users.routes", "users"),
        ), name="users"),
        path("admin/", admin.site.urls),
    )
            + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
            + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
else:
    urlpatterns = (
            [

                path("i18n/", include("django.conf.urls.i18n")),
            ] +
            i18n_patterns(
                path('accounts/', include('allauth.urls')),
                path('', include(
                    ("app.dj_apps.users.routes", "users"),
                ), name="users"),
                path("admin/", admin.site.urls),
            )
            + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
            + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )

handler404 = visu_404
