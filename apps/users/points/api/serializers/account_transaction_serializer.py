from rest_framework import serializers
from apps.users.points.api.serializers.general_serializer import (
    ExtededPropertiesSerializer, ExtendedpropertiesCreateSerializer)

from apps.users.points.models import AccountTransaction


class AccountTransactionSerializer(serializers.ModelSerializer):
    extended_properties = ExtededPropertiesSerializer(
        many=True, required=False)

    class Meta:
        model = AccountTransaction
        fields = ['id', 'status', 'account', 'value', 'available_value',
                  'transaction_source', 'transaction_type', 'expirationDate', 'extended_properties']
        read_only_fields = ['expirationDate']

    def validate_available_value(self, available_value):
        value = int(self.get_initial()['value'])

        if available_value > value:
            raise serializers.ValidationError(
                "the available value is greather than value")

        return available_value

    def create(self, validated_data):
        validated_extended_properties = validated_data.pop(
            'extended_properties')
        transaction = super().create(validated_data)
        extended_properties = []

        for prop in validated_extended_properties:
            prop['account_transaction'] = transaction.id
            extended_properties.append(prop)

        serialize_props = ExtendedpropertiesCreateSerializer(
            data=extended_properties, many=True)

        serialize_props.is_valid(raise_exception=True)
        serialize_props.save()

        return transaction
