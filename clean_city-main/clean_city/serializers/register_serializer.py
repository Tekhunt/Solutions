from rest_framework import serializers
import re
from rest_framework.fields import USE_READONLYFIELD
from clean_city.models.user_model import User


class RegisterSerializer(serializers.ModelSerializer):
    
    user_type = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'city', 'user_type']

    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise serializers.ValidationError("Enter a valid email address")
        return email
        
    def validate_phone(self, phone):
        regex = re.compile(r'^\+?[0-9]+$')
        if regex.match(phone):
            return phone
        raise serializers.ValidationError("Enter a valid phone number")
