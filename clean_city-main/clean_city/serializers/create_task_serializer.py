from clean_city.models import Task, User, CleaningArea, CheckList
from rest_framework import serializers
from django.db.models import Q


class AssigedToSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CreateTaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.ListField()
    cleaning_areas = serializers.ListField()

    class Meta:
        model = Task
        fields = ['title', 'description', 'location', 'assigned_to',
                  'start_date', 'end_date', 'cleaning_areas']

    def validate_assigned_to(self, assigned_to):
        if not assigned_to:
            raise serializers.ValidationError("Assigned to is required")
        return list(assigned_to)


class CleaningAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningArea
        fields = ['name', 'checklist']


class CreateTaskSerializerRes(serializers.ModelSerializer):
    cleaning_area = CleaningAreaSerializer(many=True)
    assigned_to = AssigedToSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'location', 'created_by',
                  'assigned_to', 'start_date', 'end_date', 'cleaning_area')


class UpdateCheckListSerializer(serializers.Serializer):
    checklist = serializers.ListField()
