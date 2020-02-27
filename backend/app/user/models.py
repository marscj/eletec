from django.db import models
# from django.contrib.auth.models import AbstractUser, Group
from auth.phone.models import PhoneNumberAbstactUser

class User(PhoneNumberAbstactUser):
    
    class Role(models.TextChoices):
        Customer = 'Customer'
        Staff = 'Staff'
        Freelancer = 'Freelancer'

    role = models.CharField(default=Role.Customer, choices=Role.choices, max_length=16)

    class Meta:
        db_table = 'user'

class Address(models.Model):

    class Model(models.TextChoices):
        Personal = 'Personal'
        Company = 'Company'

    class Style(models.TextChoices):
        Apartment = 'Apartment'
        Villa = 'Villa'

    model = models.CharField(default=Model.Personal, choices=Model.choices, max_length=16)

    city = models.TextField(blank=True, null=True)

    community = models.TextField(blank=True, null=True)

    street = models.TextField(blank=True, null=True)

    building = models.TextField(blank=True, null=True)

    office_no = models.TextField(blank=True, null=True)

    style = models.CharField(default=Style.Apartment, choices=Style.choices, max_length=16)

    villa_no = models.TextField(blank=True, null=True)

    lat = models.FloatField(blank=True, null=True)

    lgt = models.FloatField(blank=True, null=True)

    address = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address', blank=True, null=True)

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

    class DaysOfWeek(models.TextChoices):
        Monday = 'Monday'
        Tuesday = 'Tuesday'
        Wednesday = 'Wednesday'
        Thursday = 'Thursday'
        Friday = 'Friday'
        Saturday = 'Saturday'
        Sunday = 'Sunday'

    useful = models.BooleanField(blank=True, null=True, default=False)

    name = models.CharField(blank=True, null=True, max_length=36)

    form = models.TimeField(blank=True, null=True)

    to = models.TimeField(blank=True, null=True)

    days_of_week = models.CharField(default=DaysOfWeek.Monday, choices=DaysOfWeek.choices, max_length=16)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worktime', blank=True, null=True)

    class Meta:
        db_table = 'worktime'