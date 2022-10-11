from django.contrib.auth.models import Group

from rest_framework import serializers

from apps.users.user.models import City, Department, Country, IdentificationType, ProfileStatus

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'postal_code', 'department']

    def to_representation(self, instance):
       data =  super().to_representation(instance)
       department = instance.department
       data['department'] = {
            'id': department.id,
            'name': department.name
       }
       return data

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'country']

    def to_representation(self, instance):
       data =  super().to_representation(instance)
       country = instance.country
       data['country'] = {
            'id':country.id,
            'name':country.name
       }
       return data

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','name']

class IdentificationtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationType
        fields = ['id','name']

class ProfileStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileStatus
        fields = ['id','name']