from django.contrib import admin
from apps.products.customer.models import City, Country, Customer, Department, IdentificationType
# Register your models here.

admin.site.register(City)
admin.site.register(Customer)
admin.site.register(Department)
admin.site.register(Country)
admin.site.register(IdentificationType)