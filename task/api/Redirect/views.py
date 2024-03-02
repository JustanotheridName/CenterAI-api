from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..UrlConversion.models import UrlConversion
from django.shortcuts import redirect

@api_view(['GET'])
def redirect_to_original(request, short_code):
    try:
        url_conversion = UrlConversion.objects.get(link_converted=short_code)
        return redirect(url_conversion.link)
    except UrlConversion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
