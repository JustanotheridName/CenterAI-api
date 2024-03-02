from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UrlConversion
from .serializer import UrlConversionReadSerializer, UrlConversionWriteSerializer

class UrlConversionCreate(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UrlConversionWriteSerializer(data=request.data)
        if serializer.is_valid():
            try:
                url_conversion = UrlConversion.objects.get(link=serializer.validated_data['link'])
                serializerRead = UrlConversionReadSerializer(url_conversion)
                return Response(serializerRead.data, status=status.HTTP_202_ACCEPTED)
            except UrlConversion.DoesNotExist:
                instance = serializer.save()
                return Response(UrlConversionReadSerializer(instance).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
