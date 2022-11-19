from rest_framework import serializers

from apps.users.points.models import AccountStatus, TransactionStatus, TransactionSource, TransactionType

class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatus 
        fields = ['id','name']

class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus 
        fields = ['id','name']

class TransactionSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSource
        fields = ['id','name']
        
class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ['id','name']