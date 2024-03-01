from rest_framework import serializers
from .models import UrlConversion

class UrlConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlConversion
        fields = [
            "link",
            "link_converted",
            "ip",
            "user_agent",
            "timestamp"
        ]