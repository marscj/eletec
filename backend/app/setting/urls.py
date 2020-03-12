from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'faqs', views.FaqView, basename='faqs')
router.register(r'apps', views.AppView, basename='apps')
urlpatterns = router.urls