from rest_framework import serializers
from apps.users.points.api.serializers.general_serializer import TransactionSourceSerializer, TransactionStatusSerializer, TransactionTypeSerializer

from apps.users.points.models import AccountTransaction
from apps.users.user.models.Profile import Profile


class AccountTransactionSerializer(serializers.ModelSerializer):
    # transaction_source = TransactionSourceSerializer()
    # transaction_type = TransactionTypeSerializer()
    # status = TransactionStatusSerializer()
    class Meta:
        model = AccountTransaction
        fields = ['id', 'status', 'account', 'value', 'available_value',
                  'transaction_source', 'transaction_type', 'expirationDate']


class AddPointsProfileSerializer(serializers.Serializer):
    profile = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all())
    value = serializers.IntegerField(min_value=1, required=True)

    class Meta:
        model = AccountTransaction
        fields = ['profile', 'value']

    def create(self, validated_data):
        profile = validated_data['profile']
        value = validated_data['value']
        transaction = AccountTransaction.objects.AddPointsProfile(
            profile=profile, value=value)
        return validated_data
