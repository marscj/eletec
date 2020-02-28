from django.db import models

from app.user.models import User
from app.order.models import Order

class Job(models.Model):

    date = models.DateTimeField(blank=True, null=True)

    card = models.CharField(blank=True, null=True, max_length=16)

    unit = models.IntegerField(blank=True, null=True)

    note = models.TextField(blank=True, null=True)

    worker = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='job', blank=True, null=True)

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='job', blank=True, null=True)

    class Meta:
        db_table = 'job'