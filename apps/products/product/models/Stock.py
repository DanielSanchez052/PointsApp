import uuid
from typing import Dict
from django.db import models
from apps.core.models import BaseModel
from .Product import Products

class StockManager(models.Manager):

    def get_stock_inventory(self) -> Dict[str,int]:
        inventory = self.aggregate(total_inventory = models.Sum('inventory'))
        return {'total_inventory': 0} if inventory['total_inventory'] == None else inventory

    def get_stock_available(self) -> Dict[str,int]:
        available = self.aggregate(total_available = models.Sum('available'))
        return {'total_available': 0} if available['total_available'] == None else available

    def get_stock_redemptions(self) -> int:
        return self.get_stock_inventory()['total_inventory'] - self.get_stock_available()['total_available']

class Stock(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    product = models.OneToOneField(Products, on_delete=models.CASCADE,verbose_name='Product', related_name='stock')
    inventory = models.PositiveIntegerField('Inventory', blank=False, null=False)
    available = models.PositiveIntegerField('Available', blank=False, null=False) 
    low_inventory_alert = models.PositiveIntegerField('Low Inventory Alert', blank=False, null=True)
    is_active = models.BooleanField(default=True)

    manage = StockManager()

    @property
    def redemptions (self) -> int:
        return self.inventory - self.available

    def __str__(self) -> str:
        return f"{self.product.name} inventario: {self.inventory} disponible: {self.available}"

    class Meta:
        verbose_name_plural='Stock'