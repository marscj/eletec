from django.db import models
# from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.conf import settings

# User = get_user_model()

from .managers import EmailAddressManager, EmailConfirmationManager

class EmailAddress(models.Model):

    # email = models.EmailField(blank=True, null=True)

    verified = models.BooleanField(default=False)

    # user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='email_address', blank=True, null=True)

    objects = EmailAddressManager()

    class Meta:
        # db_table = 'email_address'
        abstract = True

    @staticmethod
    def create_otp_email(self, to_email):
        otp = get_random_string(4, '0123456789')
        from_phone = settings.DEFAULT_FROM_EMAIL
    
    def send_confirmation(self, request=None, signup=False):
        confirmation = EmailConfirmationHMAC(self)
        confirmation.send(request, signup=signup)
        return confirmation

# class EmailConfirmation(models.Model):
    
#     sent = models.DateTimeField(blank=True, null=True)

#     key = models.CharField(blank=True, null=True, unique=True, max_length=64)

#     created = models.DateTimeField(auto_now_add=True)

#     email_address = models.ForeignKey(EmailAddress, related_name='email_address', on_delete=models.SET_NULL, brank=True, null=True)

#     objects = EmailConfirmationManager()

#     class Meta:
#         db_table = 'email_confirmation'

#     def __str__(self):
#         return "confirmation for %s" % self.email_address

#     @classmethod
#     def create(cls, email_address):
#         key = get_random_string(64).lower()
#         return cls._default_manager.create(email_address=email_address, key=key)

#     def key_expired(self):
#         expiration_date = self.sent \
#             + datetime.timedelta(days=app_settings
#                                  .EMAIL_CONFIRMATION_EXPIRE_DAYS)
#         return expiration_date <= timezone.now()

#     def confirm(self, request):
#         if not self.key_expired() and not self.email_address.verified:
#             email_address = self.email_address
#             get_adapter(request).confirm_email(request, email_address)
#             return email_address

#     def send(self, request=None, signup=False):
#         get_adapter(request).send_confirmation_mail(request, self, signup)
#         self.sent = timezone.now()
#         self.save()

# class EmailConfirmationHMAC:

#     def __init__(self, email_address):
#         self.email_address = email_address

#     @property
#     def key(self):
#         return signing.dumps(
#             obj=self.email_address.pk,
#             salt= '~28cUebFxB!FUiei')

#     @classmethod
#     def from_key(cls, key):
#         try:
#             max_age = (
#                 60 * 60 * 24 * app_settings.EMAIL_CONFIRMATION_EXPIRE_DAYS)
#             pk = signing.loads(
#                 key,
#                 max_age=max_age,
#                 salt=app_settings.SALT)
#             ret = EmailConfirmationHMAC(EmailAddress.objects.get(pk=pk))
#         except (signing.SignatureExpired,
#                 signing.BadSignature,
#                 EmailAddress.DoesNotExist):
#             ret = None
#         return ret

#     def confirm(self, request):
#         if not self.email_address.verified:
#            self.email_address.verified = True
#            self.email_address.save()

#     def send(self, request=None, signup=False):
#         get_adapter(request).send_confirmation_mail(request, self, signup)