from django.db import models
from django.utils.crypto import get_random_string

from app.user.models import User

class Order(models.Model):

    STATUS_SHEET = (
        (1, 'New'),
        (2, 'Confirm'),
        (3, 'Complete'),
        (4, 'Pending'),
        (5, 'Cancel'),
        (6, 'Delete'),
    )

    status = models.IntegerField(blank=True, null=True, choices=STATUS_SHEET, default=1)
    
    cagetory = models.IntegerField(blank=True, null=True)

    info = models.TextField(blank=True, null=True)

    subInfo = models.TextField(blank=True, null=True)

    other_info = models.TextField(blank=True, null=True)

    from_date = models.DateTimeField(blank=True, null=True)

    to_date = models.DateTimeField(blank=True, null=True)

    addr = models.TextField(blank=True, null=True)

    image = models.ImageField(blank=True, null=True)

    code = models.CharField(blank=True, null=True, default=get_random_string(length=4))

    evaluation = models.TextField(blank=True, null=True)

    elv = models.IntegerField(blank=True, null=True)

    lat = models.FloatField(blank=True, null=True)

    lgt = models.FloatField(blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)

    change_at = models.DateTimeField(auto_now=True)

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='order', blank=True, null=True)







