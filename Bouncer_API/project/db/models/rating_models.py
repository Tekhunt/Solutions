from django.db import models
import uuid
from .product import Product


class Rating(models.Model):
    rating_id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    score= models.DecimalField(max_digits = 2,decimal_places = 1)
    product = models.ForeignKey(Product, on_delete = models.CASCADE ,related_name="product")
    review = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = "Ratings"
    
    def __str__(self):
        return f'rating for {self.product.name}'
        