from rest_framework import serializers
from clean_city.models import Task, User, CleaningArea, CheckList


class CleaningAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningArea
        fields = "__all__"