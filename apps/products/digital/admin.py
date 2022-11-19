from django.contrib import admin
from apps.products.digital.models import CodeStatus, Expiration, ProductCode
from apps.products.admin import productAdmin


# Register your models here.
productAdmin.register(CodeStatus)
productAdmin.register(Expiration)
productAdmin.register(ProductCode)
