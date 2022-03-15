from rest_framework import serializers
from clean_city.models import User
import cloudinary.uploader
import re


class EditProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    profile_image = serializers.ImageField(required=False) or serializers.URLField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'city', 'profile_image', 'sex']

    def validate_phone(self, phone):
        if phone:
            if not re.match(r'^([0-9\(\)\/\+ \-]*)$', phone):
                raise serializers.ValidationError("Invalid phone number. Please ensure you enter a valid phone number.")
        return phone

    def validate_profile_image(self, profile_image):
        try:
            image = cloudinary.uploader.upload(profile_image)
            return image["url"]
        except Exception as error:
            raise serializers.ValidationError(str(error))

    def to_representation(self, obj):
        return {"username": obj.username,
                "first_name": obj.first_name,
                "last_name": obj.last_name,
                "phone": obj.phone,
                "email": obj.email,
                "city": obj.city,
                "profile_image": obj.profile_image,
                "sex": obj.sex,
                }
