import uuid
from django.db import models

class NotificationType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    name = models.CharField(max_length=150, unique=True, blank=True)
    config = models.TextField('config',max_length=500, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}|{self.is_active}'

    class Meta:
        verbose_name='Notification Type'
        verbose_name_plural='Notification Type'