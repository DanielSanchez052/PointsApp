from datetime import datetime

from django.db import models 
from apps.core.models import BaseModel
from apps.users.user.models import Profile
from .AccountStatus import AccountStatus

class AccountManager(models.Manager):
    def getPoints(self, profile):
        points = self.prefetch_related('accounttransaction_set')\
            .filter(
                models.Q(accounttransaction__status_id = 1) &
                models.Q(user = profile)
            ).exclude(
                    accounttransaction__expirationDate__lte = datetime.now()) \
            .annotate(total = models.Sum('accounttransaction__available_value'))\
            .values('total')
        return points[0]['total'] if len(points) > 0 else 0



class Account(BaseModel):
    status = models.ForeignKey(AccountStatus, on_delete=models.SET_DEFAULT, default=1)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    objects = AccountManager()

    def __str__(self) -> str:
        return f'{self.user}|{self.status.name}'

    class Meta:
        verbose_name='Account'
        verbose_name_plural='Accounts'