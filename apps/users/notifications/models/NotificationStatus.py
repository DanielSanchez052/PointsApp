import uuid
from django.db import models

class NotificationStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    name = models.CharField(max_length=150, unique=True, blank=True)

    def __str__(self) -> str:
        return f'{self.id}|{self.name}'

    class Meta:
        verbose_name='Notification status'
        verbose_name_plural='Notification status'