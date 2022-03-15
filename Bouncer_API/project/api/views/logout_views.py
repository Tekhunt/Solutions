from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import AnonymousUser



@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == 'GET':
        request.user.auth_token.delete()
        return Response({"success": ("Successfully logged out.")}, status= status.HTTP_200_OK)