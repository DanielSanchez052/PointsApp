import uuid
from django.db import models


class IdentificationType(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Identification Type'
        verbose_name_plural = 'Identification Type'
