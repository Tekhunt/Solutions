from django.db import models
import uuid, datetime
from .brand import Brand
from .category_model import Category


class Product(models.Model):
    LARGE ='L'
    MEDIUM = 'M'
    SMALL = 'S'
    SIZE_CHOICES = [
        (LARGE , 'Large'), 
        (MEDIUM , 'Medium'), 
        (SMALL , 'Small'),
    ]
    WHITE = 'WH'
    BLUE = 'BL'
    RED ='RE'
    BLACK= 'BK'
    BROWN = 'BR'
    COLOUR_CHOICES = [
        (WHITE, 'White'),
        (BLUE , 'Blue'), 
        (RED , 'Red'), 
        (BLACK, 'BK'), 
        (BROWN , 'Brown'),
    ] 

    
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=30, unique = True)

    image = models.URLField(max_length=256)
    price = models.FloatField(default=0.0, null=True)
    ratings = models.FloatField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE,  null = True)
    # label = models.ForeignKey(Label, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()

    discounted_price = models.DecimalField(max_digits=10, decimal_places=4)
    shipping_fee = models.FloatField(default='', null=True)
    size = models.CharField(max_length=30,choices=SIZE_CHOICES,default=MEDIUM)
    description = models.TextField(max_length=256, default='', null=True)
    
    colour = models.CharField(max_length=30,choices=COLOUR_CHOICES,default=BLACK)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name
