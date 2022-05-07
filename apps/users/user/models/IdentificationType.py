import uuid
from django.db import models

class IdentificationType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    name = models.CharField(max_length=150, unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}|{self.is_active}'

    class Meta:
        verbose_name='Identification Type'
        verbose_name_plural='Identification Type'