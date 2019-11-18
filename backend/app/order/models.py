from django.db import models
from django.utils.crypto import get_random_string

from app.user.models import User

class Order(models.Model):

    STATUSHEET = (
        (1, 'NEW'),
        (2, 'CONFIRM'),
        (3, 'COMPLETE'),
        (4, 'PENDING'),
        (5, 'CANCEL'),
        (6, 'DELETE'),
    )

    status = models.IntegerField(blank=True, null=True, choices=STATUSHEET, default=1)
    
    cagetory = models.IntegerField(blank=True, null=True)

    info = models.TextField(blank=True, null=True)

    subInfo = models.TextField(blank=True, null=True)

    fromDate = models.DateTimeField(blank=True, null=True)

    toDate = models.DateTimeField(blank=True, null=True)

    addr = models.TextField(blank=True, null=True)

    image = models.ImageField(blank=True, null=True)

    otherInfo = models.TextField(blank=True, null=True)

    code = models.CharField(blank=True, null=True, default=get_random_string(length=4))

    evaluation = models.TextField(blank=True, null=True)

    elv = models.IntegerField(blank=True, null=True)

    lat = models.FloatField(blank=True, null=True)

    lgt = models.FloatField(blank=True, null=True)

    staff = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='order', blank=True, null=True)

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='order', blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)

    change_at = models.DateTimeField(auto_now=True)







