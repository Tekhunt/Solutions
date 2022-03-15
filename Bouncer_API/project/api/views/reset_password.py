from rest_framework import generics, status
from db.models.user_model import User
from rest_framework.response import Response
from db.serializers.reset_password_serializer import ResetPasswordSerializer


class PasswordResetAPI(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, otp):
        try:
            if User.objects.get(otp_code=otp):
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid()
                return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'Token is not valid, please request a new one'},
                            status=status.HTTP_401_UNAUTHORIZED)

