import uuid
from django.db import models
from pkg_resources import require
from apps.users.custom_auth.models import Auth
from apps.core.models import BaseModel
from .City import City
from .ProfileStatus import ProfileStatus
from .IdentificationType import IdentificationType


class Profile(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE, related_name='profile')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.SET_DEFAULT, default=1)
    status = models.ForeignKey(ProfileStatus, on_delete=models.SET_DEFAULT, default=1)
    identification = models.CharField('identification', max_length=150, unique=True)
    name = models.CharField('name', max_length=150)
    last_name = models.CharField('last name',max_length=150, blank=True)
    phone = models.CharField('phone number', max_length=50)
    phone2 = models.CharField('phone extra', max_length=50, blank=True, null=True)
    email = models.CharField('email', max_length=250, unique=True, blank=True)
    address = models.CharField('address', max_length=250, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return f'{self.identification}|{self.name} {self.last_name}'

    class Meta:
        verbose_name='Profile'
        verbose_name_plural='Profiles'