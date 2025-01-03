from app.dj_apps.users.models import Client
from django.http import Http404


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]
        subdomain = host.split('.')[0]
        try:
            request.tenant = Client.objects.get(subdomain=subdomain)
        except Client.DoesNotExist:
            raise Http404("Tenant not found")

        response = self.get_response(request)
        return response
