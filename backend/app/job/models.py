from django.db import models

from app.contract.models import Contract
class Job(models.Model):

    date = models.DateTimeField(blank=True, null=True)

    card = models.CharField(blank=True, null=True, max_length=16)

    unit = models.IntegerField(blank=True, null=True)

    note = models.TextField(blank=True, null=True)

    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, related_name='job', blank=True, null=True)


