import uuid

from django.db import models


class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=6, unique=True, default=None)
    email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} with id {self.user_id}'
