from clean_city.models import Task, CleaningArea
from rest_framework import serializers

from .admin_view_all_users_serializer import AdminViewAllUsersSerializer
from .create_task_serializer import UpdateCheckListSerializer


class UpdateAssignedTaskSerializer(serializers.ModelSerializer):
    checklist = serializers.ListField()
    task_status = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = ['checklist', 'task_status']

    def to_representation(self, obj):
        return{
            "title": obj.title,
            "description": obj.description,
            "location": obj.location,
            "assigned_to": AdminViewAllUsersSerializer(obj.assigned_to.all(), many=True).data,
            "start_date": obj.start_date,
            "end_date": obj.end_date,
            "created_by": obj.created_by.username,
            "cleaning_area": CleaningAreaSerializer(obj.cleaning_area.all(), many=True).data,
            "task_status": obj.task_status
        }


class CleaningAreaSerializer(serializers.ModelSerializer):
    task_status = serializers.CharField(required=False)

    class Meta:
        model = CleaningArea
        fields = ('__all__')


