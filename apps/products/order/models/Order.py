from django.db import models
from apps.core.models import BaseModel
from apps.products.customer.models import Customer 
from .OrderStatus import OrderStatus

class Order(BaseModel):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_DEFAULT, default=1)
    ordered_date = models.DateField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"{self.reference_number}"

    @property
    def reference_number(self) -> str:
        return f"ORDER--{self.pk}"

    @property
    def total_price(self):
        total_cost = sum(item.get_total_price for item in self.items.all())
        return total_cost
    
    @property
    def description(self):
        return ", ".join(
            [f"{item.quantity}x {item.product.name}" for item in self.items.all()]
        )


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ("-created_at",)