from django.http.response import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from uritemplate import partial
from clean_city.permissions.manager_permission import IsManager
from clean_city.permissions.accept_task_permissions import IsCleaner, IsGarbageCollector
from clean_city.models import Task, User, CheckList, CleaningArea
from clean_city.serializers.update_task_serializer import UpdateTaskSerializer
from clean_city.serializers.create_task_serializer import CreateTaskSerializerRes
from clean_city.serializers.update_assigned_task_serializer import UpdateAssignedTaskSerializer


def check_sender(task, request):
    if request.user.is_admin:
        return 'admin'
    elif request.user == task.created_by:
        return 'creator'
    elif request.user in task.assigned_to.all():
        return 'assigned'
    return False


def update_all_tasks(task, request, serializer):
    if request.data.get('cleaning_area') is not None:
        task.cleaning_area.clear()
        cleaning_area = request.data.get('cleaning_area', None)
        for area in cleaning_area:
            if CheckList.objects.filter(place=area).exists():
                checklist = CheckList.objects.get(place=area)
                create_clean_areas = CleaningArea.objects.create(
                    name=checklist.place, checklist=checklist.list)
                task.cleaning_area.add(create_clean_areas)
                task.save()

    if request.data.get('assigned_to') is not None:
        task.assigned_to.clear()
        assigned_to = request.data.get('assigned_to', None)
        for user_pk in assigned_to:
            task.assigned_to.add(User.objects.get(pk=user_pk))
            task.save()
    if request.data.get('title') is not None or request.data.get('description') is not None or request.data.get('location') is not None or request.data.get('start_date') is not None or request.data.get('end_date') is not None:
        task.title = request.data.get('title', task.title)
        task.description = request.data.get('description', task.description)
        task.location = request.data.get('location', task.location)
        task.start_date = request.data.get('start_date', task.start_date)
        task.end_date = request.data.get('end_date', task.end_date)
        task.save()
    return task


def update_all_check_list_and_status(request, task):
    task_status = request.data.get('task_status', None)
    if request.data.get('checklist') is not None:
        checklist = request.data.get('checklist', None)
        for places in checklist:
            if task.cleaning_area.filter(name=places.get('name')).exists():
                update_list = task.cleaning_area.get(
                    name=places.get('name'))
                update_list.checklist = places.get('checklist')
                update_list.save()
        if task_status is not None:
            task.task_status = task_status
            task.save()
        get_updated_check_lists = task.cleaning_area.all()
        get_update_task_staus = task.task_status
        data = {
            "checklist": get_updated_check_lists.values(),
            "task_status": get_update_task_staus
        }
        return data


class UpdateTaskApiView(generics.GenericAPIView):
    permission_classes = [IsAdminUser |
                          IsManager | IsCleaner | IsGarbageCollector]

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get_serializer_class(self):
        if self.request.user.is_cleaner or self.request.user.is_bin_collector:
            return UpdateAssignedTaskSerializer
        if self.request.user.is_manager or self.request.user.is_admin:
            return UpdateTaskSerializer

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = self.get_serializer_class()(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        task = Task.objects.filter(id=kwargs['pk'])[0]
        serializer = self.get_serializer_class()(task, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            if check_sender(task, request) == "assigned":
                res = update_all_check_list_and_status(request, task)
                return Response(dict(res), status=status.HTTP_200_OK)
            elif check_sender(task, request) == "creator" or check_sender(task, request) == "admin":
                update_all_tasks(task, request, serializer)
                return Response(dict(CreateTaskSerializerRes(task).data), status=status.HTTP_200_OK)
            else:
                return Response({'error': 'you are not authorized to update this task'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
