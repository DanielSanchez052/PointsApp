import django.contrib.auth.password_validation as validators
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from rest_framework import serializers

from apps.users.custom_auth.api.serializers.authentication_serializer import PasswordField
from apps.users.custom_auth.models import Auth
from apps.users.notifications.models import Notification
from .profile_serializers import ProfileSerializer
from apps.users.user.tasks import send_welcome_email

class CreateUserSerializer(serializers.ModelSerializer):
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')
    profile = ProfileSerializer(required=False)

    class Meta:
        model = Auth
        fields = ['username','email','password1','password2','profile']

   

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

    def create_profile(self,user,validated_data):
        profile = validated_data.pop('profile')
            
        profile['auth'] = user
        user_profile = ProfileSerializer.create(ProfileSerializer(),profile)
        return user_profile

    def create(self,validated_data):
        try:
            #create user Auth
            user = Auth.objects.create_user(
                username = validated_data['username'],
                email = validated_data['email'],
                password = validated_data['password']
            )
            
            if 'profile' in validated_data:
                self.create_profile(user, validated_data)

            #Send Welcome Email
            send_welcome_email.delay(
                validated_data['username'],
                validated_data['email'],
                validated_data['password'],
                user_id=user.id
            )
            
            return user
        except Exception as e:
            print(e.args[0])
            return e

