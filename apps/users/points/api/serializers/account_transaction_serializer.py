from rest_framework import serializers

from apps.users.points.models import AccountTransaction
from apps.users.user.api.serializers.profile_serializers import ListUserProfileSerializer
from apps.users.user.models.Profile import Profile

class AccountTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTransaction
        fields = ['id','status','account','value','available_value','expirationDate']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = {
            'id': instance.status.id,
            'name': instance.status.name
        }
        return data

class AddPointsProfileSerializer(serializers.Serializer):
    # profile = serializers.UUIDField(format='hex_verbose')
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    value = serializers.IntegerField(min_value=1, required = True)
    class Meta:
        model = AccountTransaction
        fields = ['profile','value']

    def create(self, validated_data):
        profile = validated_data['profile']
        value = validated_data['value']
        transaction = AccountTransaction.objects.AddPointsProfile(profile=profile, value=value)
        return validated_data
  