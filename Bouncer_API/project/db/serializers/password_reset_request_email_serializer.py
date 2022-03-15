from rest_framework import serializers


class ResetPasswordEmailRequestSerializer(serializers.Serializer):

    email = serializers.EmailField(min_length=2)

    email = serializers.EmailField(min_length=2, )

    email = serializers.EmailField(min_length=2, )

    class Meta:
        fields = ['email']
