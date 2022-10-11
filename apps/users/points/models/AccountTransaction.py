import uuid
from datetime import datetime, timedelta

from django.db import models 
from django.core.exceptions import ObjectDoesNotExist

from apps.core.models import BaseModel
from .Account import Account
from .TransactionStatus import TransactionStatus

class PointManager(models.Manager):
        
    def AddPointsProfile(self, profile, value):
        account = Account.objects.get(user = profile)
        transaction = self.create(status_id = 1, account = account, value=value, available_value=value)
        return transaction

class AccountTransaction(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    status = models.ForeignKey(TransactionStatus, on_delete=models.SET_DEFAULT, default=1)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(blank=True, null=True)
    available_value = models.PositiveIntegerField(blank=True, null=True)
    expirationDate = models.DateField('Expire at', blank=True, null=True, default=(datetime.now()+timedelta(days=365)))
    objects = PointManager()

    def __str__(self) -> str:
        return f'{self.account.user}|{self.value}|{self.available_value}|{self.expirationDate}'

    class Meta:
        verbose_name='Account Transaction'
        verbose_name_plural='Account Transaction'

