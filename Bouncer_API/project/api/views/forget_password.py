from rest_framework import generics, status
from rest_framework.response import Response
from db.models.user_model import User
# from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from db.serializers.password_reset_request_email_serializer import ResetPasswordEmailRequestSerializer
import random


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=data['to_email'])
        email.send()


class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def generateOtp(self):
        arr = [i for i in range(1000, 999999)]
        token = random.choice(arr)
        return str(token)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            # uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            otp = self.generateOtp()
            user.otp_code = otp
            user.save()
            current_site = get_current_site(request=request).domain
            # relative_link = reverse('password-reset-confirm',kwargs={'otp': otp})
            front_end_link = "#"
            relative_link = 'frontend/'
            absurl = f'<a href={front_end_link}>http://{current_site}/{relative_link}/?otp={otp}</a>'

            # front_end_link = '#'
            # front_end_namae ='Bouncer/'
            # relative_link = f'<a href={front_end_link} > {front_end_namae} </a>/?otp={otp}'

            # absurl = "http://" + current_site + relative_link
            email_body = "Hello, \n Use the link to reset your password \n" + absurl
            data = {'email_body': email_body, 'to_email': [
                user.email], 'email_subject': 'Reset your password'}
            Util.send_email(data)
            return Response({'success': 'we have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        else:
            return Response({'failed': 'You are not registered user'}, status=status.HTTP_400_BAD_REQUEST)
