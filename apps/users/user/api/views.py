from django.db.models import Q

from rest_framework import generics

from .serializers.user_serializers import CreateUserSerializer
from .serializers.general_serializers import CountrySerializer, RoleSerializer, CitySerializer, DepartmentSerializer, IdentificationtypeSerializer, ProfileStatusSerializer
from apps.core.permissions import CustomModelPermissions
from ..permissions import RegisterUserPermission

class RegisterUserView(generics.CreateAPIView):
    permission_classes = [RegisterUserPermission]
    serializer_class=CreateUserSerializer

class GetRoleView(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = RoleSerializer
    queryset = serializer_class.Meta.model.objects.all()

class GetCities(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = CitySerializer
    queryset = serializer_class.Meta.model.objects.filter(Q(is_active = 1) & Q(department__is_active=1))
    
class GetDepartments(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = DepartmentSerializer
    queryset = serializer_class.Meta.model.objects.filter(Q(is_active = 1) & Q(country__is_active=1))
    
class GetCounties(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = CountrySerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active = 1)

class GetIdentificationTypes(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = IdentificationtypeSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active = 1)

class GetProfileStatus(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = ProfileStatusSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active = 1)

