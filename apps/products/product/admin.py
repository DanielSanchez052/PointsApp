from django.contrib import admin
from apps.products.product.models import Brand, Category, PriceType, Products, Provider, Stock

# Register your models here.
admin.site.register(Brand)
admin.site.register(Provider)
admin.site.register(Category)
admin.site.register(PriceType)
admin.site.register(Products)
admin.site.register(Stock)
