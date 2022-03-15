from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from clean_city.models import User
from clean_city.serializers.password_reset_serializers import ForgotPasswordSerializer, PasswordResetSerializer
from utils import Util


class ForgotPasswordAPIView(APIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                user.otp = Util.generate_otp()
                user.save()

                data = {'email_subject': 'Clean City Password Reset Token',
                        'email_body': f'''Hi {user.first_name},\n
                            We received a request for a password reset.\n
                            Use the code to fully reset your password.\n
                            <b>{user.otp}</b>
                        ''',
                        'to_email': [email]
                        }
                Util.send_email(data)
                return Response({'success': f'otp code has been sent to {email}'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'email does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetAPIView(APIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, email):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data['otp_or_old_password']
            password = serializer.validated_data['new_password']
            try:
                user = User.objects.get(email=email)
                if user.otp == otp or user.password == Util.encode_password(otp):
                    user.password = Util.encode_password(password)
                    user.password_changed = True
                    user.save()
                    return Response({'success': 'password reset successful'}, status=status.HTTP_202_ACCEPTED)
                return Response({'error': 'incorrect otp or old password'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({'error': 'user with this email does not exist'})
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
