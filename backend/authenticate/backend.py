import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class AuthBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        phone_number = kwargs.get('phone_number')

        if username:
            return self._authenticate_by_username(**kwargs)
        elif email:
            return self._authenticate_by_email(**kwargs)
        elif phone_number:
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
            user = UserModel._default_manager.create(phone_number=phone_number, username=phone_number)
        else:
            if user.check_otp(phone_number, otp) and self.user_can_authenticate(user):
                return user