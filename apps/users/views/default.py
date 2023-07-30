from rest_framework.views import APIView
from rest_framework.response import Response


class DefaultView(APIView):
    """
    Default view for the users app.
    """
    authentication_classes = ()
    permission_classes = ()


    def get(self, request):
        return Response({"message": "No tenants found."})
