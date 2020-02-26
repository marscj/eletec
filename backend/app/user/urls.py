from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'', views.UserView, basename='users')
router.register(r'groups', views.UserGroupView, basename='group')
router.register(r'permissions', views.PermissionView, basename='permission')

urlpatterns = [
    url(r'info', views.UserInfoView.as_view(), name='info'),
    url(r'logout', views.UserLogoutView.as_view(), name='logout')
]
urlpatterns = urlpatterns + router.urls