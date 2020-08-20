from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

import django_filters

from .models import Image
from .serializers import ImageSerializer
from middleware.permission import CustomModelPermissions

class ContentFilter(django_filters.FilterSet):
    object_id = django_filters.NumberFilter('object_id')
    content_type = django_filters.CharFilter('content_type__model')

class ImageView(ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Image.objects.all()

    filter_class = ContentFilter