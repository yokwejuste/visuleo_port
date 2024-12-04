from django.urls import path

from apps.users.views.index import index

urlpatterns = [
    path("", index, name="index"),
]
