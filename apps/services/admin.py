from django.contrib import admin

from .models import ServiceDefinition, ServiceResults
# Register your models here.

admin.site.register(ServiceResults)
admin.site.register(ServiceDefinition)

