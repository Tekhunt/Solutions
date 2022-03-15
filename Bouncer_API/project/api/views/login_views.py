from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from db.models.user_model import User
import jwt, datetime
import bcrypt
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.hashers import check_password, make_password

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password'] 
        

        user = User.objects.filter(email=email).first()
        db_password = user.password
        email_verified = user.email_verified
        
        # confirm_pw = check_password(db_password, password)

        if user is None or not email_verified:
            raise AuthenticationFailed('User not found!')
        print(user)
        if not bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')):
            raise AuthenticationFailed('Incorrect password!')
        
        refresh = RefreshToken.for_user(user)

        response =  {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        }
        return Response({"payload":response})
    