from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

import django_filters

from .models import Order
from .serializers import OrderSerializer
from middleware.permission import CustomModelPermissions

class OrderFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')
    status = django_filters.NumberFilter('status')
    from_date__gte = django_filters.DateTimeFilter('from_date', lookup_expr='gte')
    from_date__lte = django_filters.DateTimeFilter('from_date', lookup_expr='lte')

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        if not user.is_superuser:
            return parent
        else:
            return parent.filter(user__id=user.id)
        
    
class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Order.objects.all()

    filter_class = OrderFilter
    search_fields = ['user__username', 'user__phone_number', 'user__first_name', 'user__last_name']