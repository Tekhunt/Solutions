from clean_city.models import Task, User
from rest_framework import serializers



class AssigedToSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk']


class UpdateTaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.ListField()
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)
    cleaning_area = serializers.ListField(required=False)
    task_status = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'location', 'assigned_to', 'created_by',
                  'start_date', 'end_date', 'cleaning_area', 'task_status']

