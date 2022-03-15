from django.db import models
import uuid
from .order_model import Order


class Payment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=30)
    fullname = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    otp_code = models.CharField(max_length=6, unique=True, null=True)
    email_verified = models.BooleanField(default=False)
    label = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.payment_status
