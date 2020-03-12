from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'users', views.UserView, basename='users')
router.register(r'groups', views.UserGroupView, basename='group')
router.register(r'permissions', views.PermissionView, basename='permission')
router.register(r'address', views.AddressView, basename='address')
router.register(r'skills', views.SkillView, basename='skill')
router.register(r'worktimes', views.WorkTimeView, basename='worktime')
router.register(r'contracts', views.ContractView, basename='contracts')
router.register(r'comments', views.CommentView, basename='comments')
router.register(r'applications', views.ApplicationView, basename='applications')

urlpatterns = [
    url(r'users/info/', views.UserInfoView.as_view(), name='info'),
    url(r'users/logout/', views.UserLogoutView.as_view(), name='logout')
]
urlpatterns = urlpatterns + router.urls