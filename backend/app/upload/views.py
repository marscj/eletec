from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

import django_filters

from .models import UploadImage
from .serializers import UploadImageSerializer
from middleware.permission import CustomModelPermissions

class UploadImageFilter(django_filters.FilterSet):
    project_id = django_filters.NumberFilter('project_id')
    
class UploadImageView(ModelViewSet):
    serializer_class = UploadImageSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = UploadImage.objects.all()

    filter_class = UploadImageFilter