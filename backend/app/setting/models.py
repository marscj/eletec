from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField

class Faq(models.Model):

    class Language(models.CharField):
        en = 'en',
        ar = 'ar',

    language = models.CharField(blank=True, null=True, default=Language.en, max_length=2)

    title = models.CharField(blank=True, null=True, max_length=128)

    content = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'faq'

class App(models.Model):

    class Tag(models.IntegerChoices):
        Advertising = 0,
        Banner = 1

    tag = models.IntegerField(null=True, blank=True, choices=Tag.choices, default=Tag.Advertising)

    image = VersatileImageField(upload_to='resource/app/', ppoi_field='app')
    
    image_ppoi = PPOIField()

    create_at = models.DateTimeField(auto_now_add=True)