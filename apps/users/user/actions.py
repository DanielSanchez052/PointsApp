import json

from django.db.models import Subquery
from apps.core.admin import require_confirmation, intermediate_view
from django.contrib import admin
from django.conf import settings
from django.contrib import messages

from apps.users.notifications.models import Notification, NotificationType
from apps.users.user.models import LoadUsers
from apps.users.custom_auth.models import Auth


@admin.action(description="Create Users Profiles")
@require_confirmation
def create_users_profile(self, request, queryset):
    batch_size = 1000
    auth_qs = self.model.objects.filter(
        pk__in=Subquery(
            queryset.filter(status=4).values('pk')
        )
    ).values('email', 'username') \
        .distinct('email', 'username')
    profile_qs = queryset.filter(status=4)

    notifications = []

    try:
        # create users of query
        auth_created, auth_list = LoadUsers.objects.create_users(auth_qs)

        config_id = settings.WELCOME_EMAIL_ID_CONFIG
        configuration_email = json.loads(
            NotificationType.objects.filter(id=config_id).first().config)

        # Add Notifications to welcome emails
        for user in auth_list:
            user_exists = Auth.objects.get(email=user.email)

            configuration_email.update({
                "email": user_exists.email,
                "username": user_exists.username,
                "password": user._password
            })

            notifications.append(
                Notification(
                    auth_id=user.id,
                    notification_status_id=settings.NOTIFICATION_PENDING,
                    notification_type_id=settings.WELCOME_EMAIL_ID_CONFIG,
                    name="welcome_email",
                    result="PENDING",
                    config=configuration_email))

        Notification.objects.bulk_create(notifications, batch_size=batch_size)
        # create profiles
        profile_created = LoadUsers.objects.create_profiles(
            auth_created, profile_qs, True)
        self.message_user(
            request, f"Successfully Created  {len(profile_created)} Profiles and Users", messages.SUCCESS)
    except Exception as e:
        messages.error(request, e.args)


@admin.action(description="change status of users")
@intermediate_view(context={"status_type": LoadUsers.CHOICE_STATUS}, confirm_template="admin/action_change_status.html")
def change_status(self, request, queryset):
    try:
        status_id = request.POST.get("type_status")
        status = dict(LoadUsers.CHOICE_STATUS)
        queryset.update(status=status_id)
        message = f"Successfully Status Changed to {status[int(status_id)]}"
        self.message_user(
            request, message, messages.SUCCESS)
    except Exception as e:
        self.message_user(
            request, f"Error: {e.args}", messages.ERROR)
