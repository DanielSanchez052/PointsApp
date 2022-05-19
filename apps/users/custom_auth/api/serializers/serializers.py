import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from apps.users.custom_auth.models import Auth

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    class Meta:
        model = Auth
        fields = ['username','password']
    
    def validate_password(self, data):
            validators.validate_password(password=data, user=Auth)
            return data

    def create(self,validated_data):
        user = Auth(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
    
    def to_representation(self,instance):
        return {
            'username': instance.username,
            'status': instance.status
        }