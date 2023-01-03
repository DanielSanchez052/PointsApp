from django.db.models import Subquery
from apps.core.admin import require_confirmation, intermediate_view
from django.contrib import admin
from django.contrib import messages
from apps.users.user.models import LoadUsers


@admin.action(description="Create Users Profiles")
@require_confirmation
def create_users_profile(self, request, queryset):
    auth_qs = self.model.objects.filter(
        pk__in=Subquery(
            queryset.filter(status=4).values('pk')
        )
    ).values('email', 'username') \
        .distinct('email', 'username')
    profile_qs = queryset.filter(status=4)
    try:
        # create users of query
        auth_created = LoadUsers.objects.create_users(auth_qs)
        # create profiles
        profile_created = LoadUsers.objects.create_profiles(
            auth_created, profile_qs, True)
        self.message_user(
            request, f"Successfully Created  {len(profile_created)} Profiles", messages.SUCCESS)
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
