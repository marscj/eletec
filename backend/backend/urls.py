from django.urls import path
from django.conf.urls import include, url
from django.views.generic import RedirectView

from app.user import views

urlpatterns = [
    url(r'^api/auth/phone/', include('auth.phone.urls')),
    url(r'^api/users/', include('app.user.urls')),
    url(r'^api/user/info', views.UserInfoView.as_view(), name='info'),
    url(r'^api/user/logout', views.UserLogoutView.as_view(), name='logout')

    # url(r'^api/rest-auth/', include('rest_auth.urls')),
    # url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),
    # url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
]
