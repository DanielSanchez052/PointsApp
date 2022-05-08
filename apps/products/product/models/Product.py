import uuid
from decimal import Decimal
from django.db import models
from apps.core.models import BaseModel
from django.core.validators import MinValueValidator,MaxValueValidator
from .Category import Category
from .PriceType import PriceType
from .Brand import Brand
from .Provider import Provider

class Products(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    price_type = models.ForeignKey(PriceType, on_delete=models.DO_NOTHING)
    name = models.CharField('Name', max_length = 255, blank = False, null = False)
    slug = models.SlugField()
    description = models.TextField('description', max_length=255, blank= False, null=False)
    price = models.DecimalField('price', max_digits=10, decimal_places=2
                                    ,validators=[MinValueValidator(Decimal('0.01'))])
    discount = models.DecimalField('discount', max_digits=3, decimal_places=2, default=0 
                                    ,validators=[MaxValueValidator(Decimal('100.00')), MinValueValidator(Decimal('0.00'))])
    terms = models.TextField('term and conditions', max_length=255, blank= True, null=True)
    instructions = models.TextField('instructions', max_length=255, blank= True, null=True)
    email_instructions = models.TextField('email instructions', max_length=500, blank= True, null=True)
    template_email = models.CharField(null=False, blank=True, max_length=50)
    cost = models.IntegerField('Cost', blank=False, null=False )
    category = models.ManyToManyField(Category, verbose_name='Category product')
    recomended = models.BooleanField('is recomended', blank=True, null=True, default=False)
    image = models.URLField('product image', max_length=255, null=False, blank = False) 
    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f"{self.name}|{self.category.description}"

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'