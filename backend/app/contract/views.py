from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authtoken import views

import django_filters

from .models import Contract
from .serializers import ContractSerializer
from middleware.permission import CustomModelPermissions

class ContractFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')

class ContractView(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Contract.objects.all()

    filter_class = ContractFilter