from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UrlConversion
from .serializer import UrlConversionReadSerializer, UrlConversionWriteSerializer
from ...Throttles.BurstRateThrottle import BurstRateThrottle
import asyncio

class UrlConversionView(APIView):
    throttle_classes = [BurstRateThrottle]

    def post(self, request, *args, **kwargs):
        serializer = UrlConversionWriteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            try:
                # url_conversion = await asyncio.get_event_loop().run_in_executor(None, UrlConversion.objects.get, link=serializer.validated_data['link'])
                url_conversion = UrlConversion.objects.get(link=serializer.validated_data['link'])
                serializerRead = UrlConversionReadSerializer(url_conversion)
                return Response(serializerRead.data, status=status.HTTP_202_ACCEPTED)
            except UrlConversion.DoesNotExist:
                # instance = await asyncio.get_event_loop().run_in_executor(None, serializer.save)
                instance = serializer.save()
                return Response(UrlConversionReadSerializer(instance).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
