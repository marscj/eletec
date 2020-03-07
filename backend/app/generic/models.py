from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from versatileimagefield.fields import VersatileImageField, PPOIField

def file_path_name(instance, filename):
    file_path = 'resource/{model}/{tag}/{id}/{filename}'.format(model=instance.content_type.model,tag=instance.tag, id=instance.object_id, filename=filename) 
    return file_path

class Image(models.Model):

    tag = models.SlugField()

    image = VersatileImageField(upload_to=file_path_name, ppoi_field='image_ppoi',)
    
    image_ppoi = PPOIField()
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'image'

@receiver(pre_delete, sender=Image)
def image_pre_delete(sender, instance, **kwargs):
    
    if instance.image is not None: 
        instance.image.delete()