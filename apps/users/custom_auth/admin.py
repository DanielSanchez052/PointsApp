from django.contrib import admin
from apps.users.custom_auth.models import Auth
from django.contrib.auth.models import Permission, Group
# Register your models here.
admin.site.register(Auth)
admin.site.register(Permission)
