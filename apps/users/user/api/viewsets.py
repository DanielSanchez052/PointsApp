from django.db.models import Q

from rest_framework import viewsets

from .serializers.profile_serializers import UpdateUserProfileSerializer, ListUserProfileSerializer, ProfileSerializer
from apps.core.mixins import SerializerActionMixin


class ProfileUserViewset(SerializerActionMixin,viewsets.ModelViewSet):
                    
    serializer_class = ListUserProfileSerializer

    serializer_action_classes = {
        'update':UpdateUserProfileSerializer,
        'partial_update':UpdateUserProfileSerializer,
        'create':ProfileSerializer
    }

    queryset=serializer_class.Meta.model.objects.filter(Q(auth__is_active=1) & Q(status=1)).select_related('auth')
