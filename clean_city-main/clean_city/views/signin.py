from clean_city.models import User
from clean_city.serializers.signin_serializer import SigninSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from django.db.models import Q
from utils import Util


class SigninApiView(APIView):
    serializer_class = SigninSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username_or_email = serializer.validated_data['username_or_email']
            password = serializer.validated_data['password']
            password = Util.encode_password(password)

            try:
                user = User.objects.get(Q(username__iexact=username_or_email) | Q(email__iexact=username_or_email))
                if not user.password_changed:
                    return Response(
                        {"error": "You have to change your password from the default password before you can login"},
                        status=status.HTTP_400_BAD_REQUEST)
                if password != user.password:
                    return Response({"error": "Incorrect password, try again."}, status=status.HTTP_400_BAD_REQUEST)
                token = str(Token.objects.get_or_create(user=user)[0])
                return Response({"username": user.username, "token": token, "user type": user.user_type()}, status=status.HTTP_200_OK)
            except User.DoesNotExist as error:
                return Response({"error": str(error)}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
