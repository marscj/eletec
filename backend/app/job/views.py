from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

import django_filters

from .models import Job
from .serializers import JobSerializer
from middleware.permission import CustomModelPermissions

class OrderFilter(django_filters.FilterSet):
    worker_id = django_filters.NumberFilter('worker_id')

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        if user.is_superuser:
            return parent
        else:
            return parent.filter(worker_id=user.id)
        
    
class JobView(ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Job.objects.all()

    filter_class = OrderFilter