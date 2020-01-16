from django.urls import path
from django.conf.urls import include, url
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^api/auth/', include('auth.phone.urls')),

    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
]
