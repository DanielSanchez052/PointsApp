from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.sessions.models import Session

from apps.users.user.admin import ProfileInline
from apps.users.custom_auth.models import Auth, IpLocked, UserSession


# Register your models here.
admin.site.register(Permission)
admin.site.register(Session)
admin.site.register(IpLocked)
admin.site.register(UserSession)

class AuthAdmin(admin.ModelAdmin):
    model= Auth
    inlines = [
        ProfileInline
    ]

admin.site.register(Auth, AuthAdmin)


