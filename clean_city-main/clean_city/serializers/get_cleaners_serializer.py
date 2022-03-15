from clean_city.models import Task, User, CleaningArea
from rest_framework import serializers
from django.db.models import Q



class GetCleanersAndBinCollectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "profile_image", "user_type", "email", "phone", "city", "created_at", "sex"]