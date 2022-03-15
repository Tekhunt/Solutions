from django.db import models
from datetime import date
import uuid

class Category(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        db_table = "bouncer_category"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        self.title
        
