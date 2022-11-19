from django.db import models

from apps.core.models import BaseModel
from apps.users.points.models.AccountTransaction import AccountTransaction


class AccountTransactionExtendedProperty(BaseModel):
    value = models.CharField(max_length=255, )
    key = models.CharField(max_length=50)
    account_transaction = models.ForeignKey(
        AccountTransaction, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.key}|{self.value}'

    class Meta:
        verbose_name = "Transaction Extended Property"
        verbose_name_plural = "Transaction Extended Properties"
