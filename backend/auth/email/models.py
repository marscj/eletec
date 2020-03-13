from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAddress(models.Model):

    email = models.EmailField(blank=True, null=True, unique=True)

    otp = models.CharField(blank=True, null=True, max_length=6)

    verified = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='email_address', blank=True, null=True)

    class Meta:
        db_table = 'email_address'
