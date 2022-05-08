import uuid
from django.db import models
from apps.core.models import BaseModel
from apps.products.customer.models import City

class Provider(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    name = models.CharField('name', max_length=150, null=True, blank=True)
    address = models.CharField('address', max_length=250, null=True, blank=True)
    nit = models.CharField('NIT', max_length=100, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    postal_code = models.CharField('Postal Code', max_length=50, null=True, blank=True)
    phone = models.CharField('Phone Number', max_length=50)
    extra = models.TextField('Extra Information', null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}|{self.postal_code} {self.is_active}'

    class Meta:
        verbose_name='Provider'
        verbose_name_plural='Provider'
        

