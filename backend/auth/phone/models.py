import datetime
import hashlib
import os

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class PhoneNumberUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, phone_number, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, phone_number, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, username, email, password, **extra_fields)

class PhoneNumberUser(models.Model):
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    objects = PhoneNumberUserManager()

    class Meta:
        abstract = True

class PhoneToken(models.Model):
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    otp = models.CharField(blank=True, null=True, max_length=6)

    class Meta:
        db_table = 'phone_token'
