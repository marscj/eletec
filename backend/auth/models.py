from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
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

class User(AbstractUser):
    
    email_verified = models.BooleanField(default=False)

    phone_number = PhoneNumberField(unique=True, blank=True, null=True)

    objects = UserManager()

    class Meta:
        abstract = True

    def send_email_confirmation(self, request):
        confirmation = EmailConfirmationHMAC(self)
        confirmation.send(request)
        return confirmation

    def send_phone_confirmation(self, request):
        

    def check_otp(self, phone_number, otp):
        confirmation = self.phone_confirmation.all().last()
        if confirmation:
            return confirmation.otp == otp and not confirmation.expired()

class PhoneConfirmation(models.Model):

    otp = models.CharField(blank=True, null=True, max_length=4)

    phone_number = PhoneNumberField(blank=True, null=True, unique=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'phone_confirmation'

    def expired(self):
        expiration_date = self.created + datetime.timedelta(days=1)
        return expiration_date <= timezone.now()

class EmailConfirmationHMAC:

    def __init__(self, user):
        self.user = user

    @property
    def key(self):
        return signing.dumps(
            obj=self.user.pk,
            salt= '~28cUebFxB!FUiei')

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
        if not self.user.email_verified:
           self.user.email_verified = True
           self.user.save()

    def send(self, request=None, signup=False):
        get_adapter(request).send_confirmation_mail(request, self, signup)