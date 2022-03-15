from rest_framework import generics, permissions, authentication
from clean_city.models import User
from clean_city.serializers.admin_view_all_users_serializer import AdminViewAllUsersSerializer


class AdminViewAllUsersAPIView(generics.ListAPIView):
    serializer_class = AdminViewAllUsersSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    filterset_fields = ["is_manager", "is_cleaner", "is_bin_collector"]
