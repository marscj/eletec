from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'uploads', views.UploadImageView, basename='uploads')
router.register(r'images', views.ImageView, basename='images')
urlpatterns = router.urls