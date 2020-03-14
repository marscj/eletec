import datetime
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from .models import PhoneToken
from .utils import model_field_attr


class PhoneBackend(ModelBackend):
    def __init__(self, *args, **kwargs):
        self.user_model = get_user_model()

    def get_phone_number_data(self, phone_number):
        """
        Method used for filtering query.
        """
        phone_number_field = getattr(settings, 'PHONE_NUMBER_FIELD', 'phone_number')
        data = {
            phone_number_field: phone_number
        }
        return data

    def get_username(self):
        """
        Returns a UUID-based 'random' and unique username.

        This is required data for user models with a username field.
        """
        return str(uuid.uuid4())[:model_field_attr(self.user_model, 'username', 'max_length')]

    def create_user(self, phone_token, **extra_fields):
        """
        Create and returns the user based on the phone_token.
        """
        password = self.user_model.objects.make_random_password()

        username = extra_fields.get('username', phone_token.phone_number)
        password = extra_fields.get('password', password)
        kwargs = {
            'username': username,
            'password': password,
        }

        phone_number = phone_token.phone_number

        kwargs.update(self.get_phone_number_data(phone_number))
        user = self.user_model.objects.create_user(**kwargs)
        return user

    def authenticate(self, request, phone_number=None, otp=None, **extra_fields):
        if not phone_number or not otp:
            return 
            
        try:
            phone_token = PhoneToken.objects.get(phone_number=phone_number, otp=otp)
        except PhoneToken.DoesNotExist:
            raise PhoneToken.DoesNotExist

        user = self.user_model.objects.filter(
            **self.get_phone_number_data(phone_token.phone_number)
        ).first()

        if not user:
            user = self.create_user(
                phone_token=phone_token,
                **extra_fields
            )
        
        phone_token.used = True
        phone_token.save()

        if self.user_can_authenticate(user):
            return user