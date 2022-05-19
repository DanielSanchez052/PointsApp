import uuid
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}|{self.is_active}'

    class Meta:
        verbose_name='User Country'
        verbose_name_plural='User Country'