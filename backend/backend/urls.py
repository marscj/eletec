from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('app.sms.urls')),
    url(r'^api/phone_login/', include('phone_login.urls')),
]
