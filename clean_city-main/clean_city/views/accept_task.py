from rest_framework import generics, status
from clean_city.models import Task
from rest_framework.response import Response
from utils import Util
from clean_city.permissions.accept_task_permissions import IsCleaner, IsGarbageCollector


class AcceptTask(generics.GenericAPIView):
    permission_classes = [IsCleaner | IsGarbageCollector]

    def get(self, request, id, bool):
        try:
            task = Task.objects.get(id=id)
            if request.user not in task.assigned_to.all():
                return Response({"error": "This task was not assigned to you, you cannot accept it."}, status=status.HTTP_403_FORBIDDEN)

            if bool == 'true':
                task.task_status = "InProgress"
                task.save()
                return Response({"Success": "Task Accepted Succesfully"}, status=status.HTTP_200_OK)
            else:
                task.assigned_to.remove(request.user)
                task.save()
                creator = task.created_by
                email_body = f'''Hi {creator.first_name}, \n
                                The task '{task.title}' was rejected by {request.user.first_name}. \n
                                Please reassign the task to another {request.user.user_type().capitalize()}\n\n
                                Thank you for using Clean City'''

                data = {'email_body': email_body, 'to_email': [creator.email],
                        'email_subject': 'Update on recently created Task'}
                Util.send_email(data)
                return Response({"Success": "Task Rejected"},status=status.HTTP_200_OK)
        except (Task.DoesNotExist, Exception) as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
