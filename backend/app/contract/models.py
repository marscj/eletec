from django.db import models

# Create your models here.
class Contract(models.Model):

    OPTIONSHEET = (
        (1, 'Economy'),
        (2, 'Standard'),
        (3, 'Premium'),
        (4, 'Customized'),
    )
    
    option = models.IntegerField(blank=True, null=True, choices=OPTIONSHEET, default=1)