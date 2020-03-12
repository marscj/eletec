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

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = User.objects.all()

    filter_class = UserFilter
            
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

class ContractView(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Contract.objects.all()

    filter_class = ContractFilter

class AddressFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')

class AddressView(ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Address.objects.all()

    filter_class = AddressFilter

class SkillFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')

class SkillView(ModelViewSet):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Skill.objects.all()

    filter_class = SkillFilter

class WorkTimeFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter('user__id')

class WorkTimeView(ModelViewSet):
    serializer_class = WorkTimeSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = WorkTime.objects.all()

    filter_class = WorkTimeFilter

class ContentFilter(django_filters.FilterSet):
    object_id = django_filters.NumberFilter('object_id')
    content_type = django_filters.CharFilter('content_type__model')

class CommentView(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Comment.objects.all()

    filter_class = ContentFilter

class ApplicationView(ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Application.objects.filter(apply=False)