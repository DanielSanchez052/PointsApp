import profile
from rest_framework import serializers 

from apps.users.user.api.serializers.profile_serializers import ProfileSerializer
from apps.users.custom_auth.models import Auth
from apps.users.points.models import Account


class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    available_points = serializers.SerializerMethodField('getAvailablePoints')

    def getAvailablePoints(self, instance):
        return Account.objects.getPoints(instance.profile)

    class Meta:
        model = Auth
        fields = ('username', 'email', 'profile', 'status', 'available_points')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = {"status": instance.status, "name": instance.get_status_display()}

        return data

    
