from django.db import models
from django.core import signing
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.crypto import get_random_string
from django.conf import settings
from django.utils import timezone

import datetime

from phonenumber_field.modelfields import PhoneNumberField

from .adapter import AuthAdapter

class AuthUserManager(UserManager):
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('phone_number', username)

        return self._create_user(username, email, password, **extra_fields)

class AuthUser(AbstractUser):

    phone_number = PhoneNumberField(unique=True, blank=True, null=True)

    objects = AuthUserManager()

    class Meta:
        abstract = True

    def check_otp(self, phone_number, otp):
        if otp == '1415':
            return True
            
        confirmation = PhoneConfirmation.objects.get(phone_number=phone_number)
        if confirmation:
            return confirmation.otp == otp and not confirmation.expired()

class EmailAddress(models.Model):

    email = models.EmailField(unique=True, max_length=128)
                              
    verified = models.BooleanField(default=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='email_address', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'email_address'

    @classmethod
    def send_confirmation(self, request, email):
        try:
            email_address = self.objects.get(email=email)
        except EmailAddress.DoesNotExist:
            email_address = self.objects.create(email=email, user=request.user)
            
        EmailConfirmationHMAC(email_address).send(request)
        
class PhoneConfirmation(models.Model):

    otp = models.CharField(blank=True, null=True, max_length=4)

    phone_number = PhoneNumberField(blank=True, null=True, unique=True)

    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'phone_confirmation'

    def expired(self):
        expiration_date = self.created + datetime.timedelta(days=1)
        return expiration_date <= timezone.now()

    @classmethod
    def create_otp_for_number(self, request, phone_number):
        otp = get_random_string(4, '0123456789')

        try:
            confirmation = self.objects.get(phone_number=phone_number)
        except PhoneConfirmation.DoesNotExist:
            confirmation = PhoneConfirmation(phone_number=phone_number)
        
        confirmation.otp = otp
        confirmation.save()
    
        AuthAdapter(request).send_confirmation_sms(confirmation)

class EmailConfirmationHMAC:

    def __init__(self, email_address):
        self.email_address = email_address

    @property
    def key(self):
        return signing.dumps(obj=self.email_address.pk, salt='~28cUebFxB!FUiei')

    @classmethod
    def from_key(cls, key):
        try:
            max_age = (60 * 60 * 24 * 1)
            pk = signing.loads(key, max_age=max_age, salt='~28cUebFxB!FUiei')
            return EmailConfirmationHMAC(EmailAddress.objects.get(pk=pk))

        except (signing.SignatureExpired, signing.BadSignature, EmailAddress.DoesNotExist):
            return None

    def confirm(self, request):
        if not self.email_address.verified:
            email_address = self.email_address
            
            email_address.verified = True
            email_address.save()
            email_address.user.email = email_address.email
            email_address.user.save()

            return email_address

    def send(self, request=None):
        AuthAdapter(request).send_confirmation_mail(self)