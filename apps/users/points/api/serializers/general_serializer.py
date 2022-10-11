from rest_framework import serializers

from apps.users.points.models import AccountStatus, TransactionStatus

class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatus 
        fields = ['id','name']

class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus 
        fields = ['id','name']