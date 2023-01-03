from rest_framework import serializers

from apps.users.points.models import Account
from .general_serializer import AccountStatusSerializer
from apps.users.user.api.serializers.profile_serializers import ProfileSerializer


class AccountSerializer(serializers.ModelSerializer):
    status = AccountStatusSerializer(read_only=True)
    user = ProfileSerializer(read_only=True)
    available_points = serializers.SerializerMethodField('getAvailablePoints')

    def getAvailablePoints(self, instance):
        return Account.objects.getPoints(instance.user)

    class Meta:
        model = Account
        fields = ['status', 'user', 'available_points']
