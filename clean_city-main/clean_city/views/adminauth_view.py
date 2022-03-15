from clean_city.models import User
from clean_city.serializers.adminauth_serializer import AdminSignupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  permissions, status
from utils import Util


class AdminSignup(APIView):
    serializer_class = AdminSignupSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            username = f"{first_name} {last_name}"
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            password = Util.encode_password(password)
           
            user = User.objects.create(first_name=first_name, last_name=last_name, 
                                    email=email, username=username, password=password 
            )
            user.is_staff = True
            user.is_superuser = True
            user.is_admin = True
            user.password_changed = True
            user.save()  
            return Response({"message": "Registration successful, you can go ahead to login."}, status=status.HTTP_201_CREATED)      
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
     