from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'', views.UserView, basename='users')
urlpatterns = router.urls