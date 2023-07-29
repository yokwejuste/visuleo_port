from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _



class HomeView(APIView):
    """
    View that returns the home page of the API.
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        return Response(
            {
                'message': _('Welcome to the Portfolio API.')
            },
            status=200
        )