import uuid
from django.db import models
from apps.core.models import BaseModel
from .City import City
from .IdentificationType import IdentificationType


class Customer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    id_user = models.UUIDField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.SET_DEFAULT, default=1)
    identification = models.CharField('identification', max_length=150, unique=True, blank=True)
    name = models.CharField('name', max_length=150, null=True, blank=True)
    last_name = models.CharField('last name',max_length=150, null=True, blank=True)
    phone = models.CharField('phone number', max_length=50)
    phone2 = models.CharField('phone extra', max_length=50)
    email = models.CharField('email', max_length=250, unique=True, blank=True)
    address = models.CharField('address', max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.identification}|{self.name} {self.last_name}'

    class Meta:
        verbose_name='Profile'
        verbose_name_plural='Profiles'