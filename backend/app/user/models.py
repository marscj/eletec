from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):

    phone_number = models.CharField(blank=True, null=True, unique=True, max_length=16)

    class Meta:
        db_table = 'user'

class Address(models.Model):

    MODEL_SHEET = (
        (1, 'Personal'),
        (2, 'Company')
    )

    STYLE_SHEET = (
        (1, 'Apartment'),
        (2, 'Villa')
    )

    model = models.IntegerField(blank=True, null=True, choices=MODEL_SHEET, default=1)

    city = models.TextField(blank=True, null=True)

    community = models.TextField(blank=True, null=True)

    street = models.TextField(blank=True, null=True)

    building = models.TextField(blank=True, null=True)

    office_no = models.TextField(blank=True, null=True)

    style = models.IntegerField(blank=True, null=True, choices=STYLE_SHEET, default=1)

    villa_no = models.TextField(blank=True, null=True)

    lat = models.FloatField(blank=True, null=True)

    lgt = models.FloatField(blank=True, null=True)

    address = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addr', blank=True, null=True)

    class Meta:
        db_table = 'address'

class Skill(models.Model):

    userful = models.BooleanField(blank=True, null=True, default=False)

    name = models.CharField(blank=True, null=True, max_length=36)

    other = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill', blank=True, null=True)

    class Meta:
        db_table = 'skill'

class WorkTime(models.Model):

    userful = models.BooleanField(blank=True, null=True, default=False)

    name = models.CharField(blank=True, null=True, max_length=36)

    form = models.TimeField(blank=True, null=True)

    to = models.TimeField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worktime', blank=True, null=True)

    class Meta:
        db_table = 'worktime'