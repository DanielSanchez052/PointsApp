from decimal import Decimal
import uuid
from django.conf import settings
from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.core.models import BaseModel
from apps.products.digital.models import ProductCode
from .Order import Order

class OrderItem(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(ProductCode,related_name="order_items", on_delete=models.CASCADE, verbose_name='product')
    unit_price = models.DecimalField("Unit Price", max_digits=10, decimal_places=2
                                    ,validators=[MinValueValidator(Decimal('0.01'))])
    quantity = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(settings.CART_ITEM_MAX_QUANTITY)])
    discount = models.DecimalField('discount', max_digits=3, decimal_places=2, default=0 
                                    ,validators=[MaxValueValidator(Decimal('100.00'))
                                                ,MinValueValidator(Decimal('0.00'))])


    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.name}"

    @property
    def get_total_price(self):
        return self.price * self.quantity 

    class Meta:
        verbose_name='OrderItem'
        verbose_name_plural='OrderItems'