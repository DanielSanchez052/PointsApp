import uuid
from jsonschema import validate, ValidationError

from django.core.exceptions import ValidationError as Error
from django.db import models
from apps.core.models import BaseModel
from apps.users.custom_auth.models import Auth
from .NotificationStatus import NotificationStatus
from .NotificationType import NotificationType
from ..strategy.strategy import CONFIGURATION_SCHEMA_BASE


class Notification(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
    notification_status = models.ForeignKey(
        NotificationStatus, on_delete=models.DO_NOTHING)
    notification_type = models.ForeignKey(
        NotificationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=255, blank=True, null=False)
    result = models.TextField(max_length=255, blank=True, null=True)
    config = models.JSONField(
        'config', blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.auth.username}|{self.name}|{self.notification_status.name}|{self.result}'

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'Notification'
        verbose_name_plural = 'Notification'

    def clean(self):
        try:
            config_value = self.config
            schema = self.notification_type.config_schema

            if not schema:
                schema = CONFIGURATION_SCHEMA_BASE

            validate(config_value, schema)
        except ValidationError as e:
            raise Error({"config": (e.message)})
        except Exception as e:
            raise Error(
                {"config": (f"Error: {e.args}")}, code="invalid")
