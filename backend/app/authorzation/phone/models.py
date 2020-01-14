import datetime
import hashlib
import os

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from sendsms.message import SmsMessage

class PhoneNumberUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, phone_number, email,
                     password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            username=username, email=email, phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone_number,
                    email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, phone_number, email, password,
                                 **extra_fields)

    def create_superuser(self, username, phone_number, email, password,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, phone_number, email, password,
                                 **extra_fields)

class PhoneNumberAbstactUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True)
    objects = PhoneNumberUserManager()

    class Meta:
        abstract = True

class PhoneToken(models.Model):
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    otp = models.CharField(blank=True, null=True, max_length=6)
    used = models.BooleanField(default=False)

    class Meta:
        db_table = 'phone_token'

    def __str__(self):
        return "{} - {}".format(self.phone_number, self.otp)

    @classmethod
    def create_otp_for_number(cls, number):

        otp = get_random_string(4, '0123456789')

        try: 
            phone_token = PhoneToken(phone_number=number)
            phone_token.otp = otp
            phone_token.save()
        except VerifyCode.DoesNotExist:
            PhoneToken.objects.create(phone_number=number, otp=otp)

        from_phone = getattr(settings, 'SENDSMS_FROM_NUMBER')

        message = SmsMessage(
            body=render_to_string(
                "otp_sms.txt",
                {"otp": otp, "id": phone_token.id}
            ),
            from_phone=from_phone,
            to=[number]

        )
        message.send()
        return phone_token

    def generate_otp(cls):
        return get_random_string(4, '0123456789')
