from apps.portfolio.views import HomeView
from django.urls import path


urlpatterns = [
    path('test/',HomeView.as_view(), name='test'),
]