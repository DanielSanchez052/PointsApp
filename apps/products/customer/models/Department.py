import uuid
from django.db import models
from .Country import Country

class Department(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}|{self.is_active}'

    class Meta:
        verbose_name='Product Department'
        verbose_name_plural='Product Departments'