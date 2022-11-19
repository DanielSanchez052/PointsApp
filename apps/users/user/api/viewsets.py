from django.db.models import Q

from rest_framework import viewsets

from .serializers.profile_serializers import UpdateUserProfileSerializer, ListUserProfileSerializer, ProfileSerializer
from apps.core.mixins import SerializerActionMixin
from apps.core.permissions import CustomModelPermissions

class ProfileUserViewset(SerializerActionMixin,viewsets.ModelViewSet):
    permission_classes = [CustomModelPermissions]
    serializer_class = ListUserProfileSerializer

    serializer_action_classes = {
        'update':UpdateUserProfileSerializer,
        'partial_update':UpdateUserProfileSerializer,
        'create':ProfileSerializer
    }

    queryset = serializer_class.Meta.model.objects.filter(Q(auth__is_active=1) & Q(status=1)).prefetch_related('auth')

    def list(self, request, *args, **kwargs):
        if(not request.user.groups.filter(name__in=['Admin','Super Admin']).exists()):
            self.queryset = self.queryset.filter(auth = self.request.user)
        return super().list(request, *args, **kwargs)
  