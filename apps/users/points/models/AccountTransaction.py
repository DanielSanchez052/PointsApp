from datetime import datetime, timedelta
from django.db import models 
from apps.core.models import BaseModel
from .Account import Account
from .TransactionStatus import *

class PointManager(models.Manager):
    pass

class AccountTransaction(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    status = models.ForeignKey(TransactionStatus, on_delete=models.SET_DEFAULT, default=1)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(blank=True, null=True)
    available_value = models.PositiveIntegerField(blank=True, null=True)
    ExpirationDate = models.DateField('Expire at', blank=True, null=True, default=(datetime.now()+timedelta(days=365)))

    def __str__(self) -> str:
        return f'{self.account.user}|{self.value}|{self.available_value}|{self.ExpirationDate}'

    class Meta:
        verbose_name='Account Transaction'
        verbose_name_plural='Account Transaction'

