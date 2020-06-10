from rest_framework import viewsets
from .models import Permission,Role,User
from .serializers import PermissionSerializer,RoleSerializer,UserSerializer


class PermissionViewset(viewsets.ModelViewSet):
    queryset= Permission.objects.all()
    serializer_class= PermissionSerializer

class RoleViewset(viewsets.ModelViewSet):
    queryset= Role.objects.all()
    serializer_class= RoleSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer
