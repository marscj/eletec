from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny

import django_filters

from .models import UploadImage, Image
from .serializers import UploadImageSerializer, ImageSerializer
from middleware.permission import CustomModelPermissions

class UploadImageFilter(django_filters.FilterSet):
    project_id = django_filters.NumberFilter('project_id')
    content = django_filters.NumberFilter('content')
    
class UploadImageView(ModelViewSet):
    serializer_class = UploadImageSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = UploadImage.objects.all()

    filter_class = UploadImageFilter

class ImageView(ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]
    queryset = Image.objects.all()