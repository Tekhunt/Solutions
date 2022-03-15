from django.db import models


class CheckList(models.Model):
    place = models.CharField(max_length=200, unique=True, blank=True, null=True)
    list = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.place

