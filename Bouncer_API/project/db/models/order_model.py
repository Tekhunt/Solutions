from django.db import models
import uuid  
from .cartmodel import Cart


class Order(models.Model):
    DELIVERY_STATUSES = [
        ('PS', 'Processing Stock'),
        ('DP', 'Delivery in Progress'),
        ('DL', 'Delivered'),
        ('ND', 'Not Delivered'),
        ('RC', 'Received'),
        ('RT', 'Returned'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255, null=True)
    delivery_status = models.CharField(
        max_length=2, choices=DELIVERY_STATUSES, null=True)
        
    def __str__(self):
        return self.delivery_status
    