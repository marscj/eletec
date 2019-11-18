from django.db import models

from app.user.models import User

class Contract(models.Model):

    OPTIONSHEET = (
        (1, 'Economy'),
        (2, 'Standard'),
        (3, 'Premium'),
        (4, 'Customized'),
    )
    
    option = models.IntegerField(blank=True, null=True, choices=OPTIONSHEET, default=1)

    date_of_issue = models.DateField(blank=True, null=True)

    date_of_expiry = models.DateField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='contract', blank=True, null=True)

