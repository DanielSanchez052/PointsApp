from django.db import models
from apps.core.models import BaseModel

class Category(BaseModel):
    description = models.CharField('Descripcion', max_length=50,unique = True,null = False,blank = False)
    slug = models.SlugField()
    
    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'