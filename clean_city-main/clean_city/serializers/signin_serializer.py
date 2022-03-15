from rest_framework import serializers

class SigninSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    