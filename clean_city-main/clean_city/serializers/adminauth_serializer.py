from rest_framework import serializers
from clean_city.models import User
from rest_framework.validators import ValidationError
from django.contrib.auth.password_validation import validate_password
import re

class AdminSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password':{'write_only': True, "validators" :[validate_password]}}
        
    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise serializers.ValidationError("Enter a valid email address.")
        
        if "@cleancityllc" not in email:
            raise serializers.ValidationError("The email is not a cleancityllc email.")
        return email
class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    