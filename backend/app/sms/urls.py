from django.conf.urls import url

from .import views

urlpatterns = [
    url('sendSms', views.sendSms.as_view(), name='sendSms')
]