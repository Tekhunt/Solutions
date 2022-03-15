from django.db import models
from datetime import date
import uuid
from .category_model import Category
    

class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "bouncer_sub_category"
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
    
    def __str__(self):
        self.title
        