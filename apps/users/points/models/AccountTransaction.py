from email.policy import default
import uuid
from datetime import datetime, timedelta

from django.db import models

from apps.core.models import BaseModel
from .Account import Account
from .TransactionStatus import TransactionStatus
from .TransactionSource import TransactionSource
from .TransactionType import TransactionType


class PointManager(models.Manager):

    def AddPointsProfile(self, profile, value, extended_properties):
        account = Account.objects.get(user=profile)
        transaction = self.create(
            status_id=1, account=account, value=value, available_value=value)
        return transaction


class AccountTransaction(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.ForeignKey(
        TransactionStatus, on_delete=models.SET_DEFAULT, default=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(blank=True, null=True)
    available_value = models.PositiveIntegerField(blank=True, null=True)
    expirationDate = models.DateTimeField(
        'Expire at', blank=True, null=True, default=(datetime.now()+timedelta(days=365)))
    transaction_source = models.ForeignKey(
        TransactionSource, on_delete=models.CASCADE, default=2)
    transaction_type = models.ForeignKey(
        TransactionType, on_delete=models.CASCADE, default=1)
    objects = PointManager()

    def __str__(self) -> str:
        return f'{self.account.user}|{self.value}|{self.available_value}|{self.expirationDate}'

    class Meta:
        verbose_name = 'Account Transaction'
        verbose_name_plural = 'Account Transaction'
