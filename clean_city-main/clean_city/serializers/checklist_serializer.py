from clean_city.models import CheckList
from rest_framework import serializers


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = "__all__"
