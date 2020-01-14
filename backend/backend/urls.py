from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/auth/', include('app.authorzation.phone.urls')),
]
