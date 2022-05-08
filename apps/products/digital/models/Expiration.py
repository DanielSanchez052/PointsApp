from datetime import datetime, timedelta
from django.db import models
from apps.core.models import BaseModel

class Expiration(BaseModel):
    ExpirationDate = models.DateField('Expire at', blank=True, null=True, default=(datetime.now()+timedelta(days=365)))
    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.ExpirationDate

    class Meta:
        verbose_name='Expiration date'
        verbose_name_plural='Expiration date'