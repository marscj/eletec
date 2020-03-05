from django.conf.urls import url

from .views import GenerateOTP, ValidateOTP

urlpatterns = [
    url(r'^auth/phone/generate/$', GenerateOTP.as_view(), name="generate"),
    url(r'^auth/phone/validate/$', ValidateOTP.as_view(), name="validate"),
]