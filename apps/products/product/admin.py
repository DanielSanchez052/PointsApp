from django.contrib import admin
from apps.products.product.models import Brand, Category, PriceType, Products, Provider, Stock
from apps.products.admin import productAdmin

# Register your models here.
productAdmin.register(Brand)
productAdmin.register(Provider)
productAdmin.register(Category)
productAdmin.register(PriceType)
productAdmin.register(Products)
productAdmin.register(Stock)
