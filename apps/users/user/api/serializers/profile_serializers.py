import json
from re import U
from rest_framework import serializers
from apps.users.points.models.Account import Account
from apps.users.user.api.serializers.general_serializers import RoleSerializer

from apps.users.user.models import Profile
from apps.users.custom_auth.models import Auth
from apps.users.points.models import AccountTransaction


class UpdateUserSerializer(serializers.ModelSerializer):
    groups = RoleSerializer(many=True)

    class Meta:
        model = Auth
        fields = ['username', 'email', 'groups']
        read_only_fields = ['groups']
        extra_kwargs = {
            'username': {'validators': []},
            'email': {'validators': []},
        }

    def validate_username(self, value):
        check_query = self.Meta.model.objects.filter(username=value)

        if self.instance:
            check_query.exclude(pk=self.instance.pk)

        if self.parent is not None and self.parent.instance is not None:
            auth = getattr(self.parent.instance, self.field_name)
            check_query = check_query.exclude(pk=auth.pk)

        if check_query.exists():
            raise serializers.ValidationError('this name already exists.')
        return value

    def validate_username(self, value):
        check_query = self.Meta.model.objects.filter(email=value)

        if self.instance:
            check_query.exclude(pk=self.instance.pk)

        if self.parent is not None and self.parent.instance is not None:
            auth = getattr(self.parent.instance, self.field_name)
            check_query = check_query.exclude(pk=auth.pk)

        if check_query.exists():
            raise serializers.ValidationError('this name already exists.')
        return value


class ProfileSerializer (serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['city', 'identification_type', 'status', 'identification',
                  'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code']

    def validate(self, data):
        data['auth'] = self.context['request'].user
        return data

    def create(self, validated_data):
        profile = super().create(validated_data)
        account = Account.objects.create(status_id=1, user_id=profile.id)
        return profile


class UpdateUserProfileSerializer (serializers.ModelSerializer):
    auth = UpdateUserSerializer(required=False)

    class Meta:
        model = Profile
        fields = ['auth', 'city', 'identification_type', 'status', 'identification',
                  'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code']
        read_only_fields = ('identification',)

    def update(self, instance, validated_data):
        # Update Auth model
        if 'auth' in validated_data:
            auth_data = validated_data.pop('auth')
            auth_instance = instance.auth
            auth = UpdateUserSerializer().update(auth_instance, auth_data)

        # Update Profile
        profile = super().update(instance, validated_data)
        return profile


class ListUserProfileSerializer (serializers.ModelSerializer):
    username = serializers.SerializerMethodField('getUsername')
    email = serializers.SerializerMethodField('getEmail')
    available_points = serializers.SerializerMethodField('getAvailablePoints')
    groups = serializers.SerializerMethodField('getGroups')

    def getUsername(self, instance):
        return instance.auth.username

    def getEmail(self, instance):
        return instance.auth.email

    def getAvailablePoints(self, instance):
        return Account.objects.getPoints(instance)

    def getGroups(self, instance):
        return instance.auth.groups.values()

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'groups', 'city', 'identification_type', 'status',
                  'identification', 'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code', 'available_points']
