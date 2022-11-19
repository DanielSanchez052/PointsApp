from django.contrib import admin

from apps.users.notifications.models import Notification, NotificationStatus, NotificationType

# Register your models here.
admin.site.register(Notification)
admin.site.register(NotificationStatus)
admin.site.register(NotificationType)
