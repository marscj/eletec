from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'contracts', views.ContractView, basename='contracts')
urlpatterns = router.urls