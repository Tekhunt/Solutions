from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from clean_city.serializers.create_task_serializer import CreateTaskSerializer, CreateTaskSerializerRes
from clean_city.models import Task, User, CheckList, CleaningArea
from rest_framework.response import Response
from clean_city.permissions.manager_permission import IsManager
from django.db.models import Q


def assign_task_to_users(task, serializer):
    for user_pk in serializer.validated_data['assigned_to']:
        task.assigned_to.add(User.objects.get(pk=user_pk))
        task.save()


def add_places_to_cleaning_area(task, serializer):
    for area in serializer.validated_data['cleaning_areas']:
        if CheckList.objects.filter(place=area).exists():
            checklist = CheckList.objects.get(place=area)
            create_clean_areas = CleaningArea.objects.create(
                name=checklist.place, checklist=checklist.list)
            task.cleaning_area.add(create_clean_areas)
            task.save()


class CreateTaskApiView(generics.GenericAPIView):
    serializer_class = CreateTaskSerializer
    permission_classes = [IsAdminUser | IsManager]

    def get(self, request, *args, **kwargs):
        get_cleaning_name = CheckList.objects.values_list('place', flat=True)
        return Response({"message": "Cleaning Areas", 'data': get_cleaning_name}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = User.objects.get(pk=request.user.id)
        if serializer.is_valid(raise_exception=True):
            task = Task.objects.create(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                location=serializer.validated_data['location'],
                start_date=serializer.validated_data['start_date'],
                end_date=serializer.validated_data['end_date'],
                created_by_id=user.id
            )
            task.save()
            assign_task_to_users(task, serializer)
            add_places_to_cleaning_area(task, serializer)
            res = CreateTaskSerializerRes(task).data
            return Response(dict(CreateTaskSerializerRes(task).data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        task.delete()
        return Response({"Response":"Task Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)