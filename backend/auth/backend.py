import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from .models import User, Confirmation

UserModel = get_user_model()

class AuthBackend(ModelBackend):

    # def create_phone_user(self, phone_token, **extra_fields):
    #     """
    #     Create and returns the user based on the phone_token.
    #     """
    #     password = self.user_model.objects.make_random_password()

    #     username = extra_fields.get('username', phone_token.phone_number)
    #     password = extra_fields.get('password', password)
    #     kwargs = {
    #         'username': username,
    #         'password': password,
    #     }

    #     phone_number = phone_token.phone_number

    #     kwargs.update(self.get_phone_number_data(phone_number))
    #     user = self.user_model.objects.create_user(**kwargs)
    #     return user

    # def authenticate(self, request, phone_number=None, otp=None, **extra_fields):
        
    #     if not phone_number or not otp:
    #         return 
            
    #     try:
    #         phone_token = PhoneToken.objects.get(phone_number=phone_number, otp=otp)
    #     except PhoneToken.DoesNotExist:
    #         raise PhoneToken.DoesNotExist

    #     user = self.user_model.objects.filter(phone_number=phone_number).last()

    #     if not user:
    #         user = self.create_user(
    #             phone_token=phone_token,
    #             **extra_fields
    #         )
        
    #     phone_token.used = True
    #     phone_token.save()

    #     if self.user_can_authenticate(user):
    #         return user
    def authenticate(self, request, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        phone_number = kwargs.get('phone_number')

        if username:
            return self._authenticate_by_username(**kwargs)
        elif email:
            return self._authenticate_by_email(**kwargs)
        elif phone:
            return self._authenticate_by_phone(**kwargs)
        
    def _authenticate_by_username(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        if username is None or password is None:
            return
        try:
             user = UserModel._default_manager.get(username=username)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def _authenticate_by_email(self, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if email is None or password is None:
            return
        try:
             user = UserModel._default_manager.get(email=email)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def _authenticate_by_phone(self, **kwargs):
        phone_number = kwargs.get('phone_number')
        otp = kwargs.get('otp')

        if phone_number is None or otp is None:
            return

        try:
             user = UserModel._default_manager.get(phone_number=phone_number)
        except UserModel.DoesNotExist:
            return
        else:
            if user.check_otp(phone_number, otp) and self.user_can_authenticate(user):
                return user