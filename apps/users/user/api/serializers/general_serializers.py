from django.contrib.auth.models import Group

from rest_framework import serializers

from apps.users.user.models import City, Department, Country, IdentificationType, ProfileStatus


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Department
        fields = ['id', 'name', 'country']


class CitySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = City
        fields = ['id', 'name', 'postal_code', 'department']


class IdentificationtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationType
        fields = ['id', 'name']


class ProfileStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileStatus
        fields = ['id', 'name']