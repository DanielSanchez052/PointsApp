from django.contrib import admin
from apps.products.customer.models import City, Country, Customer, Department, IdentificationType
from apps.products.admin import productAdmin
# Register your models here.

productAdmin.register(City)
productAdmin.register(Customer)
productAdmin.register(Department)
productAdmin.register(Country)
productAdmin.register(IdentificationType)
