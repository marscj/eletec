from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/auth/', include('auth.phone.urls')),
    # url(r'^phone_login/', include('phone_login.urls')),
]
