from django.db import models

# Create your models here.
class Faq(models.Model):

    class Language(models.TextChoices):
        en = 'en',
        ar = 'ar',

    language = models.CharField(blank=True, null=True, choices=Language.choices, default=Language.en, max_length=4)

    title = models.CharField(blank=True, null=True, max_length=128)

    content = models.CharField(blank=True, null=True, max_length=256)

    class Meta:
        db_table = 'faq'