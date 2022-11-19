from django.contrib import admin
from apps.products.order.models import Order, OrderItem, OrderStatus
from apps.products.admin import productAdmin

# Register your models here.
productAdmin.register(Order)
productAdmin.register(OrderItem)
productAdmin.register(OrderStatus)
