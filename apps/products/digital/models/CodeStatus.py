from django.db import models
from apps.core.models import BaseModel

class CodeStatus(BaseModel):
    name = models.CharField('name', max_length=50,unique = True,null = False,blank = False)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Code Status'
        verbose_name_plural='Code Status'