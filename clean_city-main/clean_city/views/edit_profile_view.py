from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import TokenAuthentication
from clean_city.models import User
from clean_city.serializers.edit_profile_serializer import EditProfileSerializer


class EditProfileApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EditProfileSerializer
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        user = request.user
        user_data = self.serializer_class(user).data
        return Response({'user_data': user_data}, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        user_data = request.user
        serializer = self.serializer_class(user_data, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                                'message': 'User data updated successfully',
                                'user_data': serializer.data
                            }
            ,status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
