from django.db import models 
from apps.core.models import BaseModel
from apps.users.user.models import Profile
from .AccountStatus import AccountStatus

class Account(BaseModel):
    status = models.ForeignKey(AccountStatus, on_delete=models.SET_DEFAULT, default="9c0797a1-bd67-42a4-8ae0-c74afe0f3c2b")
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user}|{self.status.name}'

    class Meta:
        verbose_name='Account'
        verbose_name_plural='Accounts'