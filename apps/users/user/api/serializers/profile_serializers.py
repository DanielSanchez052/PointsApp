from email import message
from rest_framework import serializers

from apps.users.user.models import Profile
from apps.users.custom_auth.models import Auth


class UpdateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Auth
        fields=['username','email','groups'] 
        read_only_fields= ['groups']
        extra_kwargs = {
            'username': {'validators':[]},
            'email': {'validators':[]},
        }

    def validate_username(self, value):
        check_query = self.Meta.model.objects.filter(username=value)

        if self.instance:
            check_query.exclude(pk = self.instance.pk)

        if self.parent is not None and self.parent.instance is not None:
            auth = getattr(self.parent.instance, self.field_name)
            check_query = check_query.exclude(pk=auth.pk) 

        if check_query.exists():
            raise serializers.ValidationError('this name already exists.')
        return value

    def validate_username(self, value):
        check_query = self.Meta.model.objects.filter(email=value)

        if self.instance:
            check_query.exclude(pk = self.instance.pk)

        if self.parent is not None and self.parent.instance is not None:
            auth = getattr(self.parent.instance, self.field_name)
            check_query = check_query.exclude(pk=auth.pk) 

        if check_query.exists():
            raise serializers.ValidationError('this name already exists.')
        return value

class ProfileSerializer (serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = ['city','identification_type', 'status', 'identification' ,'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code']
        
    def validate(self, data):
        data['auth'] = self.context['request'].user
        return data 

class UpdateUserProfileSerializer (serializers.ModelSerializer):
    auth = UpdateUserSerializer(required=False)

    class Meta:
        model=Profile
        fields = ['auth','city','identification_type', 'status', 'identification' ,'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code']
        read_only_fields = ('identification',)

    def update(self, instance, validated_data):
        ##Update Auth model
        if 'auth' in validated_data:
            auth_data = validated_data.pop('auth')
            auth_instance = instance.auth
            auth = UpdateUserSerializer().update(auth_instance, auth_data)

        ##Update Profile
        profile =  super().update(instance, validated_data)
        return profile


class ListUserProfileSerializer (serializers.ModelSerializer):
    auth = UpdateUserSerializer(required=True)
    class Meta:
        model=Profile
        fields = ['id','auth','city','identification_type', 'status', 'identification' ,'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        auth = data.pop('auth')
        data['username'] = auth['username']
        data['email'] = auth['email']
        data['roles'] = auth['groups']
        return data


class UniqueNestedValdiator:
    message = 'This field must be unique.'
    requires_context = True
    
    def __init__(self, base, queryset):
        self.queryset = queryset
        self.base = base

    
