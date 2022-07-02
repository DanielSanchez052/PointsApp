from django.contrib.auth import authenticate, password_validation
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.users.custom_auth.api.authentication import default_user_authentication_rule

class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['required'] = kwargs.get('required', True)
        kwargs['min_length'] = 8
        kwargs.setdefault("style", {})
        kwargs["style"]["input_type"] = "password"
        kwargs["write_only"] = True
        kwargs["trim_whitespace"] = False
        kwargs['label'] = kwargs.get('label','Password') 

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


class ChangePasswordSerializer(serializers.Serializer):
    old_password = PasswordField(label='old_password')
    new_password1 = PasswordField(label='new_password1')
    new_password2 = PasswordField(label='new_password2')

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user