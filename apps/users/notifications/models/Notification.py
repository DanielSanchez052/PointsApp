import uuid
from django.db import models
from apps.users.user.models import Profile
from apps.core.models import BaseModel
from .NotificationStatus import NotificationStatus
from .NotificationType import NotificationType

class Notification(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    notification_status = models.ForeignKey(NotificationStatus, on_delete=models.DO_NOTHING)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True, blank=True)
    description = models.TextField(max_length=255, blank=True, null=False)
    config = models.TextField('config',max_length=500, blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.name}|{self.postal_code}|{self.is_active}'

    class Meta:
        verbose_name='Notification'
        verbose_name_plural='Notification'