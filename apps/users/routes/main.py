from django.urls import path

from apps.users.views.index import index, signin, signup

urlpatterns = [
    path("", index, name="index"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
]
