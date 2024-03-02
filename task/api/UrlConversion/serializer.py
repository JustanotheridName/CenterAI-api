from rest_framework import serializers
from .models import UrlConversion
from ..Helpers.UrlConversion import UrlConversionHelper

class UrlConversionWriteSerializer(serializers.ModelSerializer):
    link = serializers.URLField()

    class Meta:
        model = UrlConversion
        fields = [
            "link",
        ]

    def validate_link(self, value):
        if not value.startswith('http:') and not value.startswith('https:'):
            raise serializers.ValidationError("Link must start with 'http:' or 'https:'")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['link_converted'] = request.build_absolute_uri('/') + UrlConversionHelper.generateRandomUrl()
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