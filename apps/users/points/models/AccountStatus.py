import uuid
from django.db import models

class AccountStatus(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
 
    def __str__(self) -> str:
        return f'{self.name}|{self.is_active}'

    class Meta:
        verbose_name='Account status'
        verbose_name_plural='Account status'