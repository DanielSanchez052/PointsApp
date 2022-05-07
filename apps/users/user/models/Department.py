import uuid
from django.db import models
from .Country import Country

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}|{self.is_active}'

    class Meta:
        verbose_name='Department'
        verbose_name_plural='Departments'