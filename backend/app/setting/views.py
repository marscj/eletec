from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny

import django_filters

from middleware.permission import CustomModelPermissions
from .models import Faq, App
from .serializers import FaqSerializer, AppSerializer

class FaqFilter(django_filters.FilterSet):
    language = django_filters.CharFilter('language')
    
class FaqView(ModelViewSet):
    serializer_class = FaqSerializer
    permission_classes = [IsAuthenticated]
    queryset = Faq.objects.all()

    filter_class = FaqFilter

class AppFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter('tag')

class AppView(ModelViewSet):
    serializer_class = AppSerializer
    permission_classes = [AllowAny]
    queryset = App.objects.all()

    ordering = ['sorter']

    filter_class = AppFilter