import uuid
from django.db import models
from apps.core.models import BaseModel
from apps.products.product.models import Products
from .Expiration import Expiration
from .CodeStatus import CodeStatus

class ProductCode(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    expiration = models.ForeignKey(Expiration, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(CodeStatus, on_delete=models.SET_DEFAULT, default=1)
    code = models.CharField('Code', max_length=500, null=True, blank=True)
    is_used = models.BooleanField('is used', default=False, null=True, blank=True)
    used_date  = models.DateField('used date', null=False, blank=False)

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name='Code Status'
        verbose_name_plural='Code Status'