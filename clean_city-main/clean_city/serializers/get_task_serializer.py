from attr import field
from clean_city.models import Task, User, CleaningArea
from rest_framework import serializers


class AssignedToSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'profile_image',
                  'user_type', 'email', 'phone', 'city']


class CleaningAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningArea
        fields = ['name', 'checklist']


class GetTaskSerializer(serializers.ModelSerializer):
    assigned_to = AssignedToSerializer(many=True)
    cleaning_area = CleaningAreaSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id','title', 'description', 'location', 'start_date',
                  'end_date', 'task_status', 'cleaning_area', 'assigned_to']
