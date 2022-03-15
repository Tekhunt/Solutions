from rest_framework import generics, status
from clean_city.models import Task, User
from rest_framework.response import Response
from clean_city.serializers.get_task_serializer import GetTaskSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


class GetUserTaskView(generics.GenericAPIView):
    serializer_class = GetTaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(email=request.user.email)
            tasks = Task.objects.filter(Q(assigned_to=user) | Q(created_by=user))
            task_list = self.serializer_class(tasks, many=True)
            return Response({"tasks": task_list.data}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
