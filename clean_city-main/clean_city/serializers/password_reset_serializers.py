from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetSerializer(serializers.Serializer):
    otp_or_old_password = serializers.CharField()
    new_password = serializers.CharField(write_only=True, validators=[validate_password])
