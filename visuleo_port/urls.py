import oauth2_provider.views as oauth2_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

ROUTE_BASE_VERSION = settings.ROUTE_BASE_VERSION

oauth2_endpoint_views = [
    path("authorize/", oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path("token/", oauth2_views.TokenView.as_view(), name="token"),
    path("revoke-token/", oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    oauth2_endpoint_views += [
        path("applications/", oauth2_views.ApplicationList.as_view(), name="list"),
        path(
            "applications/register/",
            oauth2_views.ApplicationRegistration.as_view(),
            name="register",
        ),
        path(
            "applications/<pk>/",
            oauth2_views.ApplicationDetail.as_view(),
            name="detail",
        ),
        path(
            "applications/<pk>/delete/",
            oauth2_views.ApplicationDelete.as_view(),
            name="delete",
        ),
    ]

    oauth2_endpoint_views += [
        path(
            "authorized-tokens/",
            oauth2_views.AuthorizedTokensListView.as_view(),
            name="authorized-token-list",
        ),
        path(
            "authorized-tokens/<pk>/delete/",
            oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete",
        ),
    ]

urlpatterns = (
        [
            path("__debug__/", include("debug_toolbar.urls")),
            path("__reload__/", include("django_browser_reload.urls")),
            path(
                "o/",
                include(
                    (oauth2_endpoint_views, "oauth2_provider"), namespace="oauth2_provider"
                ),
            ),
            (
                path("admin/", admin.site.urls)
                if settings.ENVIRONMENT == "local"
                else path("", include([]))
            ),
            # path(ROUTE_BASE_VERSION, include("apps.portfolio.routes")),
            path(ROUTE_BASE_VERSION, include("apps.users.routes")),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
