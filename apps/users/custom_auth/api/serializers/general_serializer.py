import profile
from rest_framework import serializers 

from apps.users.user.api.serializers.profile_serializers import ProfileSerializer
from apps.users.custom_auth.models import Auth
from apps.users.points.models import Account

class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = Auth
        fields = ('username', 'email', 'profile', 'status',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = {"status": instance.status, "name": instance.get_status_display()}
        data['available_points'] = Account.objects.getPoints(instance.profile)
        return data

    
