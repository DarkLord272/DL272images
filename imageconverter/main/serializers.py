from rest_framework import serializers


class ResizeSerializer(serializers.Serializer):
    image = serializers.ImageField()
    left = serializers.CharField(required=False, allow_blank=True)
    right = serializers.CharField(required=False, allow_blank=True)
    top = serializers.CharField(required=False, allow_blank=True)
    bottom = serializers.CharField(required=False, allow_blank=True)
    wnsize = serializers.CharField(required=False, allow_blank=True)
    hnsize = serializers.CharField(required=False, allow_blank=True)
