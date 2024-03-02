from rest_framework import serializers
from .models import UrlConversion
from ..Helpers.UrlConversion import UrlConversionHelper

class UrlConversionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlConversion
        fields = [
            "link",
        ]

    def create(self, validated_data):
        validated_data['link_converted'] = UrlConversionHelper.generateRandomUrl()
        return super().create(validated_data)

class UrlConversionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlConversion
        fields = [
            "id",
            "link",
            "link_converted",
            "timestamp"
        ]