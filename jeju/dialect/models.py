from django.db import models
from django.conf import settings

class Dictionary(models.Model):
    name = models.CharField(max_length=30)
    contents = models.CharField(max_length=50)
    def __str__(self):
        return self.name+",",self.contents
