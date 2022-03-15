from django.db import models
import uuid

class Brand(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=30, unique = True)

    def __str__(self):
        return self.name
        