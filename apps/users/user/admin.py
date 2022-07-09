from django.contrib import admin
from apps.users.user.models import City, Department, Country, IdentificationType, Profile, ProfileStatus

# Register your models here.
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(IdentificationType)
admin.site.register(Profile)
admin.site.register(ProfileStatus)


class ProfileInline(admin.StackedInline):
    model = Profile
    min_num = 0
    max_num = 1