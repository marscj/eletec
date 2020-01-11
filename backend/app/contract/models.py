from django.db import models

from app.user.models import User

class Contract(models.Model):

    class Option(models.TextChoices):
        Economy = 'Economy'
        Standard = 'Standard'
        Premium = 'Premium'
        Customized = 'Customized'

    option = models.CharField(blank=True, null=True, max_length=16, choices=Option.choices, default=Economy)

    issue_date = models.DateField(blank=True, null=True)

    expiry_date = models.DateField(blank=True, null=True)

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='contract', blank=True, null=True)

    @property
    def visit(self):
        return [0,0,0,0]