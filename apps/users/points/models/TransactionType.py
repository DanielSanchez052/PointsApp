from django.db import models 

class TransactionType (models.Model):
    name = models.CharField('name', max_length=150)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'    
    
    class Meta:
        verbose_name='Transaction Type'
        verbose_name_plural='Transaction Type'
