from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailToken(models.Model):

    email = models.EmailField(blank=True, null=True, unique=True)

    otp = models.CharField(blank=True, null=True, max_length=6)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='email_token', blank=True, null=True)

    class Meta:
        db_table = 'phone_token'
