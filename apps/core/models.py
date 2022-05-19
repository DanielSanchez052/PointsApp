import uuid
from django.db import models
#from simple_history.models import HistoricalRecords

# Create your models here.

class BaseModel(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    id = models.AutoField(primary_key=True)
    created_at = models.DateField('created at',auto_now_add=True,auto_now=False)
    modified_at = models.DateField('modified at',auto_now_add=False ,auto_now=True)
    deleted_at = models.DateField('deleted at',auto_now_add=False, auto_now=True)
    #historical = HistoricalRecords(inherit=True)

    # @property
    # def _history_user(self):
    #     return self.changed_by

    # @_history_user.setter
    # def _history_user(self, value):
    #     self.changed_by = value

    class Meta:
        abstract = True
        verbose_name='Base Model'
        verbose_name_plural = 'Base Model'