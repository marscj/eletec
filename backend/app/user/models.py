from django.db import models
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

    defAddr= models.BooleanField(default=False)

    onMap = models.BooleanField(default=False)

    model = models.CharField(default=Model.Personal, choices=Model.choices, max_length=16)

    city = models.TextField(blank=True, null=True)

    community = models.TextField(blank=True, null=True)

    street = models.TextField(blank=True, null=True)

    building = models.TextField(blank=True, null=True)

    style = models.CharField(default=Style.Apartment, choices=Style.choices, max_length=16)

    roomNo = models.TextField(blank=True, null=True)

    lat = models.FloatField(blank=True, null=True)

    lgt = models.FloatField(blank=True, null=True)

    address = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address', blank=True, null=True)

    class Meta:
        db_table = 'address'

class Skill(models.Model):
    
    class SkillSheet(models.TextChoices):
        AC = 'A/C'
        Electrical = 'Electrical'
        Plumbing = 'Plumbing'
        Cleaning = 'Cleaning'
        Duct = 'Duct Cleaning'
        Other = 'Other'

    useful = models.BooleanField(blank=True, null=True, default=False)

    skill = models.CharField(default=SkillSheet.AC, choices=SkillSheet.choices, max_length=16)

    remark = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill', blank=True, null=True)

    class Meta:
        db_table = 'skill'
        unique_together = ('skill', 'user_id')

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

    week = models.CharField(default=DaysOfWeek.Monday, choices=DaysOfWeek.choices, max_length=16)

    form = models.TimeField(blank=True, null=True)

    to = models.TimeField(blank=True, null=True)    

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worktime', blank=True, null=True)

    class Meta:
        db_table = 'worktime'
        unique_together = ('week', 'user_id')

class Contract(models.Model):

    class Option(models.TextChoices):
        Economy = 'Economy'
        Standard = 'Standard'
        Premium = 'Premium'
        Customized = 'Customized'

    option = models.CharField(blank=True, null=True, max_length=16, choices=Option.choices, default=Option.Economy)

    issue_date = models.DateField(blank=True, null=True)

    expiry_date = models.DateField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='contract', blank=True, null=True)

    class Meta:
        db_table = 'contract'

    @property
    def visit(self):
        return [0,0,0,0]