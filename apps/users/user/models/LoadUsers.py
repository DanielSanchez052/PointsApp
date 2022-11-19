import uuid
from django.db import models


class LoadUsers(models.Model):

    CHOICE_STATUS = (
        (1, 'OK'),
        (2, 'ERROR'),
        (3, 'CARGADO'),
        (4, 'LOADING'),
    )

    # auth
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField('email', max_length=250, unique=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    # profile
    identification_type = models.CharField(
        max_length=150, blank=True)
    identification = models.CharField(
        'identification', max_length=150, unique=True)
    city = models.CharField(max_length=150)
    name = models.CharField('name', max_length=150)
    last_name = models.CharField('last name', max_length=150, blank=True)
    phone = models.CharField('phone number', max_length=50)
    phone2 = models.CharField(
        'phone extra', max_length=50, blank=True, null=True)
    address = models.CharField('address', max_length=250, blank=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    status = models.SmallIntegerField(
        'load status', choices=CHOICE_STATUS, default=4)

    def __str__(self) -> str:
        return f'{self.email}|{self.username}|{self.identification_type}|{self.identification}|{self.status}'

    class Meta:
        verbose_name = 'LoadUser'
        verbose_name_plural = 'LoadUser'
