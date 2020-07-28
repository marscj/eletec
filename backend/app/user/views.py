from django.contrib.auth import logout
from django.contrib.auth.models import Group, Permission

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authtoken import views

import django_filters

from .models import User, Address, Skill, WorkTime, Contract, Comment, Application
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer, AddressSerializer, SkillSerializer, WorkTimeSerializer, ContractSerializer, CommentSerializer, ApplicationSerializer
from middleware.permission import CustomModelPermissions

class UserFilter(django_filters.FilterSet):
    role = django_filters.NumberFilter('role')

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        if user.is_superuser:
            return parent
        else:
            return parent.filter(id=user.id)

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = User.objects.all()

    filter_class = UserFilter
    search_fields = ['username', 'phone_number', 'email', 'first_name', 'last_name']
            
class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None): 
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class UserGroupView(ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Group.objects.all()

class PermissionView(ModelViewSet):
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Permission.objects.filter(content_type__model__in=['user', 'group', 'order', 'job', 'contract'])

class ContractFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        if user.is_superuser:
            return parent
        else:
            return parent.filter(user__id=user.id)

class ContractView(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]
    queryset = Contract.objects.all()

    filter_class = ContractFilter

class AddressFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        if user.is_superuser:
            return parent
        else:
            return parent.filter(user__id=user.id)

class AddressView(ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()

    filter_class = AddressFilter

class SkillFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        if user.is_superuser:
            return parent
        else:
            return parent.filter(user__id=user.id)

class SkillView(ModelViewSet):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    queryset = Skill.objects.all()

    filter_class = SkillFilter

class WorkTimeFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        if user.is_superuser:
            return parent
        else:
            return parent.filter(user__id=user.id)

class WorkTimeView(ModelViewSet):
    serializer_class = WorkTimeSerializer
    permission_classes = [IsAuthenticated]
    queryset = WorkTime.objects.all()

    filter_class = WorkTimeFilter

class CommentFilter(django_filters.FilterSet):
    object_id = django_filters.NumberFilter('object_id')
    content_type = django_filters.CharFilter('content_type__model')

class CommentView(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()

    filter_class = CommentFilter

class ApplicationFilter(django_filters.FilterSet):

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        if user.is_superuser:
            return parent.filter(apply=False)
        else:
            return parent.filter(user__id=user.id, apply=False)
            
class ApplicationView(ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Application.objects.all()

    filter_class = ApplicationFilter

    