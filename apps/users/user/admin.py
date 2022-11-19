from django.contrib import admin

from apps.users.user.models import City, Department, Country, IdentificationType, Profile, ProfileStatus, LoadUsers


class ProfileInline(admin.StackedInline):
    model = Profile
    min_num = 0
    max_num = 1


# Register your models here.
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(IdentificationType)
admin.site.register(Profile)
admin.site.register(ProfileStatus)


@admin.register(LoadUsers, site=admin.site)
class LoadUsersModelAdmin(admin.ModelAdmin):
    # resource_class = LoadUsersResource
    list_display = ['email', 'username', 'identification_type', 'identification',
                    'city', 'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code', 'status']


@admin.register(City, site=admin.site)
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'postal_code', 'department', 'is_active']
