from django.db import models
from .checklist_model import CheckList


class CleaningArea(models.Model):
    name = models.CharField(max_length=200)
    checklist = models.JSONField(default=dict, blank=True, null=True)
    
    def __str__(self):
        return self.name
