from django.db import models

# Create your models here.
class Faq(models.Model):

    class Language(models.CharField):
        en = 'en',
        ar = 'ar',

    language = models.CharField(blank=True, null=True, default=Language.en, max_length=2)

    title = models.CharField(blank=True, null=True, max_length=128)

    content = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'faq'