from django.db import models

# Create your models here.
class Contract(models.Model):
    option = models.IntegerField(blank=True, null=True)