from rest_framework import serializers

from apps.users.points.models import AccountStatus, TransactionStatus, TransactionSource, TransactionType, AccountTransactionExtendedProperty


class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatus
        fields = ['id', 'name']


class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = ['id', 'name']


class TransactionSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSource
        fields = ['id', 'name']


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ['id', 'name']


class ExtendedPropertiesListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        extended_properties = [AccountTransactionExtendedProperty(
            **prop) for prop in validated_data]

        return AccountTransactionExtendedProperty.objects.bulk_create(
            extended_properties)


class ExtededPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTransactionExtendedProperty
        fields = ['value', 'key']


class ExtendedpropertiesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTransactionExtendedProperty
        fields = ['value', 'key', 'account_transaction']
        list_serializer_class = ExtendedPropertiesListSerializer
