from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
# router.register(r'sendSms', views.sendSms.as_view(), basename='sendSms')