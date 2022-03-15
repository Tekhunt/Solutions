from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from clean_city.models import User
from django.http.response import Http404
from clean_city.serializers.deactivate_user_serializer import DeactivateUserSerializer


class DeactivateUserAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def delete(self, request, *args, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        user = self.get_object(kwargs['pk'])
        serializer = DeactivateUserSerializer(
            user, data=request.data, partial=True)
        user.is_active = False
        user.save()
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
