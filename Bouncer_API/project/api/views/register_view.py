from db.models.user_model import User
from rest_framework import views, permissions, status
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer
import random, datetime

def generate_token():
    arr = [i for i in range(1000, 999999)]
    token = random.choice(arr)
    return token

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=data['to_email'])
        email.send()

class RegisterView(APIView):
    def post(self, request):
        token= str(generate_token())
        new_data = {**request.data, "otp_code": token}
        serializer = UserSerializer(data={**request.data, "otp_code": token}) #get data from the request
        serializer.is_valid(raise_exception=True) #validate the data
        serializer.save()  #saves data
        print(serializer.data)
        
        try:
            email= request.data.get('email')
            user=User.objects.get(email=email)
            email_body=f'hey,  {user.first_name} \n\n We need to verify your email address so that you can use Bounce. \n This is your OTP  {token}. click on this link to verify http://127.0.0.1:18000/verify-otp '
            data={'email_body':email_body,'to_email':[user.email],'email_subject':'Verify your email'}
            Util.send_email(data)
            
            return Response({"message": "Registration successful, check your email for comfirmation"}, status=status.HTTP_201_CREATED)      
        
        except:
            return Response({"message":"User does not exist, Register to get access."}, status=status.HTTP_404_NOT_FOUND)
