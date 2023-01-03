from django.contrib import admin
from apps.users.points.models import Account, AccountStatus, AccountTransaction, TransactionStatus, TransactionSource, TransactionType, AccountTransactionExtendedProperty


class ExtendedPropertiesInLine(admin.StackedInline):
    model = AccountTransactionExtendedProperty
    min_num = 0


class AccountTransactionInLine(admin.StackedInline):
    model = AccountTransaction
    min_num = 0


# Register your models here.
admin.site.register(AccountStatus)
admin.site.register(AccountTransactionExtendedProperty)


@admin.register(TransactionType)
class AccountTransactionTypeAdmin(admin.ModelAdmin):
    model = TransactionType
    list_display = ['id', 'name']


@admin.register(TransactionStatus)
class AccountTransactionStatusAdmin(admin.ModelAdmin):
    model = TransactionStatus
    list_display = ['id', 'name']


@admin.register(TransactionSource)
class AccountTransactionSourceAdmin(admin.ModelAdmin):
    model = TransactionSource
    list_display = ['id', 'name']


@admin.register(AccountTransaction)
class AccountTransactionAdmin(admin.ModelAdmin):
    model = AccountTransaction
    inlines = [
        ExtendedPropertiesInLine
    ]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    model = Account
    inlines = [
        AccountTransactionInLine
    ]
