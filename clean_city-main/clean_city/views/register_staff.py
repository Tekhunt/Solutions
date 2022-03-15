from rest_framework.response import Response
from utils import Util
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from clean_city.serializers.register_serializer import RegisterSerializer


class RegisterStaffView(generics.GenericAPIView):
    """Create new user in the system"""
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data['first_name'].capitalize()
            last_name = serializer.validated_data['last_name'].capitalize()
            username = f"{first_name} {last_name}"
            email = serializer.validated_data['email']
            phone = serializer.validated_data['phone']
            city = serializer.validated_data['city']
            user_type = serializer.validated_data['user_type']
            otp = Util.generate_otp()
            password = Util.generate_password()
            email_body = f'''Hey {first_name}, \n 
                            You have just been registered on our Clean City Platform as a {user_type.capitalize()}. \n
                            If you haven't already downloaded the app, you can download from google playstore or the iOS app store 
                            and start making our cities cleaner. \n 
                            Log in with this password: {password} \n 
                            If you are prompted to reset your password, 
                            please reset your password using this otp: {otp}'''

            data = {'email_body': email_body, 'to_email': [email],
                    'email_subject': 'Reset Password'}
            try:
                Util.send_email(data)
                user = get_user_model().objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=Util.encode_password(password),
                phone=phone,
                city=city,
                otp=otp,
            )
                if user_type == "cleaner":
                    user.is_cleaner = True
                if user_type == "manager":
                    user.is_manager = True
                if user_type == "garbage collector":
                    user.is_bin_collector = True
                user.save()
                return Response({"success": f"{username} successfully added as {user_type.capitalize()}"}, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)  
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
