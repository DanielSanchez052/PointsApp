from django.contrib import admin
from apps.products.digital.models import CodeStatus, Expiration, ProductCode

# Register your models here.
admin.site.register(CodeStatus)
admin.site.register(Expiration)
admin.site.register(ProductCode)
