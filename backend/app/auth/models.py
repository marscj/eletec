from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):

    phone = models.CharField(blank=True, null=True, max_length=16)

    roles = AbstractUser.groups
    groups = None

    class Meta:
        db_table = 'users'
        ordering = ['-id']