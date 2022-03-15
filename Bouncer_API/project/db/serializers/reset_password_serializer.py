import bcrypt
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import get_object_or_404
from db.models.user_model import User


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=15, write_only=True)
    otp = serializers.CharField(min_length=6, max_length=15, write_only=True)

    class Meta:
        fields = ['password', 'otp']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            otp = attrs.get('otp')
        except Exception:
            raise AuthenticationFailed('Verification failed', 401)

        user = get_object_or_404(User, otp_code=otp)

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        user.password = hashed_password
        user.save()
        return user
