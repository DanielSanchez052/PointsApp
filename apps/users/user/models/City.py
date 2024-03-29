from django.db import models
from .Department import Department


class City(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True, blank=True)
    postal_code = models.CharField(max_length=50, unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.pk}'

    class Meta:
        verbose_name = 'User City'
        verbose_name_plural = 'User Cities'
