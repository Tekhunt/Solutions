from django.db import models
import uuid
from .user_model import User


class Cart (models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    products = models.JSONField(encoder=None, decoder=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost = models.FloatField()
    coupon = models.BooleanField(default=False)

    class Meta:
        app_label = 'db'
    
    def __str__(self):
        return self.products
    
