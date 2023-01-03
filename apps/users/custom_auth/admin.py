from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.sessions.models import Session

from import_export.admin import ImportExportModelAdmin

from apps.users.user.admin import ProfileInline
from apps.users.custom_auth.models import Auth, IpLocked, UserSession


@admin.register(Auth)
class AuthAdmin(ImportExportModelAdmin):
    model = Auth
    search_fields = ['email', 'username']
    list_display = ('email', 'username', 'status',
                    'is_active', 'created_at', 'attempts')
    #list_filter = ['email', 'username']
    ordering = ['created_at']
    list_per_page = 100
    inlines = [
        ProfileInline
    ]


# Register your models here.
admin.site.register(Permission)
admin.site.register(Session)
admin.site.register(IpLocked)
admin.site.register(UserSession)
