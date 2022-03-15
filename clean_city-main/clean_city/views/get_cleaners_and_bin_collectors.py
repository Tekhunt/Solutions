from rest_framework import generics, authentication
from clean_city.models import User
from clean_city.serializers.get_cleaners_serializer import GetCleanersAndBinCollectorsSerializer
from clean_city.permissions.manager_permission import IsManager
from rest_framework.permissions import IsAdminUser


class GetCleanersAndBinCollectorsAPIView(generics.ListAPIView):
    serializer_class = GetCleanersAndBinCollectorsSerializer
    permission_classes = [IsAdminUser | IsManager]
    queryset = User.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    filterset_fields = ["is_cleaner", "is_bin_collector"]