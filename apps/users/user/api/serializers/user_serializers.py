
import django.contrib.auth.password_validation as validators
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.users.custom_auth.api.serializers.authentication_serializer import PasswordField
from apps.users.custom_auth.models import Auth
from .profile_serializers import ProfileSerializer


class UserListSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True, many=True)
    class Meta:
        model = Auth
        fields = ('username', 'profile', 'status',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = {"status": instance.status, "name": instance.get_status_display()}
        return data

class CreateUserSerializer(serializers.ModelSerializer):
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')

    class Meta:
        model = Auth
        fields = ['username','email','password1','password2']
    
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'password2': _("The two password fields didn't match.")})
        validators.validate_password(data['password1'], self.context['request'].user)
        
        data['password'] = data.pop('password1')
        data.pop('password2')
        return data

    def validate_password(self, data):
            validators.validate_password(password=data, user=Auth)
            return data

    def create(self,validated_data):
        user = Auth(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user