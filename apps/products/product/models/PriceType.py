from django.db import models
from apps.core.models import BaseModel

class PriceType(BaseModel):
    name = models.CharField('name', max_length=50,unique = True,null = False,blank = False)
    description = models.CharField('Descripcion', max_length=255,unique = True,null = False,blank = False)
    
    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name='Price Type'
        verbose_name_plural='Price Type'