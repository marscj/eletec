from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'jobs', views.JobView, basename='orders')
urlpatterns = router.urls