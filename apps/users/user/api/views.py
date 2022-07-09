from rest_framework import generics

from .serializers.user_serializers import CreateUserSerializer
from .serializers.general_serializers import RoleSerializer
from apps.core.permissions import CustomModelPermissions
from ..permissions import RegisterUserPermission

class RegisterUserView(generics.CreateAPIView):
    permission_classes = [RegisterUserPermission]
    serializer_class=CreateUserSerializer

class GetRoleView(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = RoleSerializer
    queryset = RoleSerializer.Meta.model.objects.all()