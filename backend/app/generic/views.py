from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

import django_filters

from .models import Image, Comment
from .serializers import ImageSerializer, CommentSerializer
from middleware.permission import CustomModelPermissions

class ImageView(ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Image.objects.all()

class CommentView(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Comment.objects.all()