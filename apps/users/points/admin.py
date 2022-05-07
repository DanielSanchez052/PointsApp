from django.contrib import admin
from apps.users.points.models import Account, AccountStatus, AccountTransaction, TransactionStatus

# Register your models here.
admin.site.register(Account)
admin.site.register(AccountStatus)
admin.site.register(AccountTransaction)
admin.site.register(TransactionStatus)