from django.contrib.auth import authenticate

from rest_framework import serializers

from apps.users.custom_auth.models import Auth
from apps.users.user.api.serializers.profile_serializers import ProfileSerializer
from apps.users.custom_auth.api.authentication import default_user_authentication_rule

class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("style", {})

        kwargs["style"]["input_type"] = "password"
        kwargs["write_only"] = True
        kwargs["trim_whitespace"] = False
        kwargs['label'] = 'Password'

        super().__init__(*args, **kwargs)

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = PasswordField()

    def validate(self, attrs):
        user = authenticate(request=self.context.get('request'),
                                username=attrs.get('username'), password=attrs.get('password'))
        if not user:
            msg = 'Access denied: wrong username or password.'
            raise serializers.ValidationError(msg, code='authorization')

        if not default_user_authentication_rule(user):
            raise serializers.ValidationError('User is disabled or not exists', code='authorization')

        return {'user': user}


class LoginUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True, many=True)
    class Meta:
        model = Auth
        fields = ('username', 'profile', 'status',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = {"status": instance.status, "name": instance.get_status_display()}
        return data
