from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

import django_filters

from middleware.permission import CustomModelPermissions
from .models import Faq
from .serializers import FaqSerializer

class FaqFilter(django_filters.FilterSet):
    language = django_filters.CharFilter('language')
    
class FaqView(ModelViewSet):
    serializer_class = FaqSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Faq.objects.all()

    filter_class = FaqFilter