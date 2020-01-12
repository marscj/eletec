from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('app.user.urls')),
]
