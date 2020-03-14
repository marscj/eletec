from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.conf import settings

User = get_user_model()

class EmailAddress(models.Model):

    email = models.EmailField(blank=True, null=True)

    otp = models.CharField(blank=True, null=True, max_length=6)

    verified = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='email_address', blank=True, null=True)

    class Meta:
        db_table = 'email_address'

    @staticmethod
    def create_otp_email(self, to_email):
        otp = get_random_string(4, '0123456789')
        from_phone = settings.DEFAULT_FROM_EMAIL

class EmailConfirmationHMAC:

    def __init__(self, email_address):
        self.email_address = email_address

    @property
    def key(self):
        return signing.dumps(
            obj=self.email_address.pk,
            salt= '')

    @classmethod
    def from_key(cls, key):
        try:
            max_age = (
                60 * 60 * 24 * app_settings.EMAIL_CONFIRMATION_EXPIRE_DAYS)
            pk = signing.loads(
                key,
                max_age=max_age,
                salt=app_settings.SALT)
            ret = EmailConfirmationHMAC(EmailAddress.objects.get(pk=pk))
        except (signing.SignatureExpired,
                signing.BadSignature,
                EmailAddress.DoesNotExist):
            ret = None
        return ret

    def confirm(self, request):
        if not self.email_address.verified:
            email_address = self.email_address
            get_adapter(request).confirm_email(request, email_address)
            signals.email_confirmed.send(sender=self.__class__,
                                         request=request,
                                         email_address=email_address)
            return email_address

    def send(self, request=None, signup=False):
        get_adapter(request).send_confirmation_mail(request, self, signup)
        signals.email_confirmation_sent.send(sender=self.__class__,
                                             request=request,
                                             confirmation=self,
                                             signup=signup)