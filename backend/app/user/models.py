from django.db import models
from django.contrib.auth.models import AbstractUser, Group

import json

class User(AbstractUser):

    phoneNumber = models.CharField(blank=True, null=True, max_length=16)

    class Meta:
        db_table = 'user'
        ordering = ['-id']

class Address(models.Model):

    MODELSHEET = (
        (1, 'PERSONAL'),
        (2, 'COMPANY')
    )

    STYLESHEET = (
        (1, 'APARTMENT'),
        (2, 'VILLA')
    )

    model = models.IntegerField(blank=True, null=True, choices=MODELSHEET, default=1)

    city = models.TextField(blank=True, null=True)

    community = models.TextField(blank=True, null=True)

    street = models.TextField(blank=True, null=True)

    building = models.TextField(blank=True, null=True)

    officeNo = models.TextField(blank=True, null=True)

    style = models.IntegerField(blank=True, null=True, choices=STYLESHEET, default=1)

    villaNo = models.TextField(blank=True, null=True)

    lat = models.FloatField(blank=True, null=True)

    lgt = models.FloatField(blank=True, null=True)

    address = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addr', blank=True, null=True)

class Skill(models.Model):

    userful = models.BooleanField(blank=True, null=True, default=False)

    name = models.CharField(blank=True, null=True, max_length=36)

    other = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill', blank=True, null=True)

class WorkTime(models.Model):

    userful = models.BooleanField(blank=True, null=True, default=False)

    name = models.CharField(blank=True, null=True, max_length=36)

    form = models.TimeField(blank=True, null=True)

    to = models.TimeField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worktime', blank=True, null=True)