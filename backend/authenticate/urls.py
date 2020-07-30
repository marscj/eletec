from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^auth/phone/generate/$', views.GeneratePhone.as_view(), name="generate_phone"),
    url(r'^auth/phone/validate/$', views.ValidatePhone.as_view(), name="validate_phone"),
    url(r'^auth/email/generate/$', views.GenerateEmail.as_view(), name="generate_email"),
    url(r'^auth/email/validate/$', views.ValidateEmail.as_view(), name="validate_email"),
    url(r'^auth/email/code/generate/$', views.GenerateCodeEmail.as_view(), name="generate_email_code"),
    url(r'^auth/email/code/validate/$', views.ValidateCodeEmail.as_view(), name="validate_email_code"),
]