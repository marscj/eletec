from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from versatileimagefield.fields import VersatileImageField, PPOIField

from app.user.models import User
from app.order.models import Order

class UploadImage(models.Model): 

    class Flag(models.IntegerChoices):
        Photo = 0
        Id = 1
        License = 2
        Source = 3
    
    class Content(models.IntegerChoices):
        User = 0
        Order = 1

    content = models.IntegerField(blank=True, null=True, choices=Content.choices, default=Content.User)

    flag = models.IntegerField(blank=True, null=True, choices=Flag.choices, default=Flag.Photo)
    
    image = VersatileImageField(blank=True, null=True, upload_to='resource/', ppoi_field='image_ppoi',)
    
    image_ppoi = PPOIField()
    
    object_id = models.IntegerField()

    class Meta:
        db_table = 'upload'

def file_path_name(instance, filename):
    file_path = 'resource/{tag}/{filename}'.format(user_id=instance.tag, filename=filename) 
    return file_path

class Image(models.Model):

    tag = models.SlugField(blank=True, null=True)

    image = VersatileImageField(blank=True, null=True, upload_to=file_path_name, ppoi_field='image_ppoi',)
    
    image_ppoi = PPOIField()
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'image'