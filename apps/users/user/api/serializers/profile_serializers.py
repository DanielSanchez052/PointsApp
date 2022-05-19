from xml.etree.ElementInclude import include
from rest_framework import serializers

from apps.users.user.models import Profile

class ProfileSerializer (serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = ['city','identification_type', 'status', 'identification' ,'name', 'last_name', 'phone', 'phone2', 'email', 'address', 'postal_code']
        #depth = 1
        