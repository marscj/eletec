from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField

from app.user.models import User
from app.order.models import Order

class UploadImage(models.Model): 

    class Flag(models.IntegerChoices):
        Photo = 0
        EmiratesID = 1
        DriverLicense = 2
        Source = 3

    flag = models.IntegerField(blank=True, null=True, choices=Flag.choices, default=Flag.Photo)
    
    image = VersatileImageField(blank=True, null=True, upload_to='resource/', ppoi_field='image_ppoi',)
    
    image_ppoi = PPOIField()
    
    object_id = models.IntegerField()

    class Meta:
        db_table = 'upload'