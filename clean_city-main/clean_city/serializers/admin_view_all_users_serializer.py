from rest_framework import serializers

from clean_city.models import User


class AdminViewAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "profile_image", "user_type", "email", "phone", "city", "created_at", "sex"]
