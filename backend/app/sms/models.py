from django.db import models

class VerifyCode(models.Model):

    verify_code = models.CharField(null=True, blank=True, max_length=4)

    phone_number = models.CharField(null=True, blank=True, unique=True, max_length=16)

    class Meta:
        db_table = 'verifycode'