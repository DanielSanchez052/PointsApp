from django.db import models
from apps.core.models import BaseModel

class Brand(BaseModel):
    name = models.CharField('name', max_length=50,unique = True,null = False,blank = False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name='Brand'
        verbose_name_plural='Brand'

