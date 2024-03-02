from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..UrlConversion.models import UrlConversion
from django.shortcuts import redirect

class RedirectView(APIView):

    def get(self, request, short_code):
        try:
            url_conversion = UrlConversion.objects.get(link_converted__icontains=short_code)
            return redirect(url_conversion.link)
        except UrlConversion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
