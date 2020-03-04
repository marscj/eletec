from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^api/auth/phone/', include('auth.phone.urls')),
    url(r'^api/', include('app.user.urls')),
    url(r'^api/', include('app.order.urls')),
    url(r'^api/', include('app.upload.urls')),

    # url(r'^api/rest-auth/', include('rest_auth.urls')),
    # url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),
    # url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)