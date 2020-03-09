from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

from versatileimagefield.fields import VersatileImageField, PPOIField

from auth.phone.models import PhoneNumberAbstactUser
from app.generic.models import Image

class User(PhoneNumberAbstactUser):
    
    class Role(models.IntegerChoices):
        Customer = 0
        Staff = 1
        Freelancer = 2
        Operator = 3

    role = models.IntegerField(blank=True, null=True, choices=Role.choices, default=Role.Customer)

    images = GenericRelation(Image, related_query_name='user')

    class Meta:
        db_table = 'user'

    @property
    def name(self):
        if self.get_full_name():
            return self.get_full_name()

        return self.username
        
class Contract(models.Model):

    class Option(models.IntegerChoices):
        Economy = 0
        Standard = 1
        Premium = 2
        Customized = 3

    option = models.IntegerField(blank=True, null=True, choices=Option.choices, default=Option.Economy)

    issue_date = models.DateField(blank=True, null=True)

    expiry_date = models.DateField(blank=True, null=True)

    address = models.CharField(blank=True, null=True, max_length=128)

    remark = models.CharField(blank=True, null=True, max_length=256)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='contract', blank=True, null=True)

    class Meta:
        db_table = 'contract'

    @property
    def contractID(self):
        return  '%d-%s' % (100000 + self.id, self.expiry_date.strftime("%y%m%d"))

class Address(models.Model):

    class Model(models.IntegerChoices):
        Personal = 0
        Company = 1

    class Style(models.IntegerChoices):
        Apartment = 0
        Villa = 1

    defAddr= models.BooleanField(default=False)

    onMap = models.BooleanField(default=False)

    model = models.IntegerField(blank=True, null=True, choices=Model.choices, default=Model.Personal)

    style = models.IntegerField(blank=True, null=True, choices=Style.choices, default=Style.Apartment)

    city = models.CharField(blank=True, null=True, max_length=32)

    community = models.CharField(blank=True, null=True, max_length=32)

    street = models.CharField(blank=True, null=True, max_length=64)

    building = models.CharField(blank=True, null=True, max_length=64)

    roomNo = models.CharField(blank=True, null=True, max_length=32)

    lat = models.FloatField(blank=True, null=True)

    lng = models.FloatField(blank=True, null=True)

    address = models.CharField(blank=True, null=True, max_length=128)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address', blank=True, null=True)

    class Meta:
        db_table = 'address'

class Skill(models.Model):
    
    class Skill(models.IntegerChoices):
        AC = 0 
        Electrical = 1
        Plumbing = 2
        Cleaning = 3
        Duct = 4
        Other = 5

    skill = models.IntegerField(blank=True, null=True, choices=Skill.choices, default=Skill.AC)

    remark = models.CharField(blank=True, null=True, max_length=256)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill', blank=True, null=True)

    class Meta:
        db_table = 'skill'
        unique_together = ('skill', 'user_id')

class WorkTime(models.Model):

    class DaysOfWeek(models.IntegerChoices):
        Monday = 0
        Tuesday = 1
        Wednesday = 2
        Thursday = 3
        Friday = 4
        Saturday = 5
        Sunday = 6

    week = models.IntegerField(blank=True, null=True, choices=DaysOfWeek.choices, default=DaysOfWeek.Monday)

    form = models.TimeField(blank=True, null=True)

    to = models.TimeField(blank=True, null=True)    

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worktime', blank=True, null=True)

    class Meta:
        db_table = 'worktime'
        unique_together = ('week', 'user_id')

def file_path_name(instance, filename):
    file_path = 'resource/{model}/{filename}'.format(model=instance.content_type.model, filename=filename) 
    return file_path

class Comment(models.Model):
    
    comment = models.CharField(blank=True, null=True, max_length=256)

    rating = models.IntegerField(blank=True, null=True, default=5)

    image = VersatileImageField(upload_to=file_path_name, ppoi_field='image_ppoi', null=True, blank=True)

    image_ppoi = PPOIField()

    create_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comment', blank=True, null=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'comment'