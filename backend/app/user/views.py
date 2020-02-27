from django.contrib.auth import logout
from django.contrib.auth.models import Group, Permission
from django.core.mail import send_mail, BadHeaderError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authtoken import views

from .models import User
from .serializers import UserSerializer, GroupDetailSerializer, PermissionSerializer
from middleware.permission import CustomModelPermissions

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = User.objects.all()
            
class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)

        print('111111')
        try:
            print('22222')
            send_mail('Subject here', 'Here is the message.', 'mobileapp@eletec.ae', ['mars.jinxing@gmail.com'], fail_silently=False)
            print('3333')
        except BadHeaderError:
            print('4444')

        return Response(serializer.data)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class UserGroupView(ModelViewSet):
    serializer_class = GroupDetailSerializer
    permission_classes = [IsAuthenticated, CustomModelPermissions]
    queryset = Group.objects.all()

class PermissionView(ModelViewSet):
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Permission.objects.filter(content_type__model__in=['user', 'group', 'vehicle', 'order', 'itinerary', 'category', 'price', 'orderitinerary', 'invoice', 'driver'])
    