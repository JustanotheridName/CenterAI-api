from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UrlConversion
from .serializer import UrlConversionSerializer

class UrlConversionCreate(APIView):

    def post(self, request, *args, **kwargs):
        queryset = UrlConversion.objects.all()
        return Response(status=status.HTTP_418_IM_A_TEAPOT)
