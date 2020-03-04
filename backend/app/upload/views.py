from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

import django_filters

from .models import Order
from .serializers import OrderSerializer
from middleware.permission import CustomModelPermissions

class OrderFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')
    
class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Order.objects.all()

    filter_class = OrderFilter