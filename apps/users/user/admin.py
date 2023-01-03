from django.contrib import admin
from django.contrib import messages

from import_export.admin import ImportExportModelAdmin

from apps.users.user.admin_import.user_import import LoadUsersResource
from apps.users.user.models import City, Department, Country, IdentificationType, Profile, ProfileStatus, LoadUsers

from .actions import create_users_profile, change_status


class ProfileInline(admin.StackedInline):
    model = Profile
    min_num = 0
    max_num = 1


# Register your models here.
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(ProfileStatus)


@admin.register(LoadUsers)
class LoadUsersAdmin(ImportExportModelAdmin):
    model = LoadUsers
    search_fields = ['email', 'username', 'identification', 'status']
    list_filter = ['status']
    resource_class = LoadUsersResource
    list_display = [
        'email', 'username', 'identification_type', 'identification',
        'city', 'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code', 'status'
    ]
    list_per_page = 100
    actions = [create_users_profile, change_status,
               'clean_users_created', 'change_status', ]

    @admin.action(description="Clean users Created")
    def clean_users_created(self, request, queryset):
        queryset.filter(status=3).delete()
        self.message_user(request, "Clean Successfully", messages.SUCCESS)


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    model = Profile
    list_display = [
        'auth', 'identification_type', 'identification',
        'city', 'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code', 'status'
    ]


@admin.register(City, site=admin.site)
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'postal_code', 'department', 'is_active']


@admin.register(IdentificationType)
class IdentificationTypeAdmin(admin.ModelAdmin):
    model = IdentificationType
    list_display = ['id', 'name']
