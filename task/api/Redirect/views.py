from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET'])
def redirect_to_original(request, short_code):
    pass
    # try:
    #     shortened_url = ShortenedURL.objects.get(short_code=short_code)
    #     return redirect(shortened_url.original_url)
    # except ShortenedURL.DoesNotExist:
    #     return Response(status=404)
    # def get(self, request, *args, **kwargs):
    #     title = request.query_params.get("title", "") # if no title empty string assigned
    #     data = UrlConversion.objects.first()
    #     serializer = UrlConversionSerializer(data)
    #     return Response(serializer.data, status=status.HTTP_418_IM_A_TEAPOT)