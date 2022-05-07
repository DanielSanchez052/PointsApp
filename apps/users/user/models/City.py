import imp
import uuid
from django.db import models
from .Department import Department 

class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True, blank=True)
    postal_code = models.CharField(max_length=50, unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}|{self.postal_code}|{self.is_active}'

    class Meta:
        verbose_name='City'
        verbose_name_plural='Cities'