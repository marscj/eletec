from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'images', views.ImageView, basename='images')
router.register(r'comments', views.CommentView, basename='comments')
urlpatterns = router.urls