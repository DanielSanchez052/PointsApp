# import uuid

# from django.db import models

# from apps.core.models import BaseModel

# # Create your models here.
# class ServiceDefinition(BaseModel):
#     STATUS_SERVICE_DEFINITION_CHOICES=[
#         (0, "Disabled"),(1, "Enabled"),(2, "Starting"),(3, "Running"),(4, "Ending")
#     ]

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
#     name = models.CharField(max_length=150, unique=True, blank=True)
#     description = models.TextField(max_length=255, blank=True, null=False)
#     status = models.SmallIntegerField(choices=STATUS_SERVICE_DEFINITION_CHOICES, default=1)
#     config = models.TextField('config',max_length=500, blank=False, null=False)
    
#     def __str__(self) -> str:
#         return f'DEFINITION -> {self.name}|{self.status}'

#     class Meta:
#         verbose_name='Services'
#         verbose_name_plural='Services'


# class ServiceResults(BaseModel):
#     STATUS_SERVICE_RESULTS_CHOICES = [
#         (0,"Error"),(1,"Pending"),(2,"Success")
#     ]
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
#     serviceDefinition = models.ForeignKey(ServiceDefinition)
#     status = models.SmallIntegerField(choices=STATUS_SERVICE_RESULTS_CHOICES, default=1)
#     result = models.TextField(max_length=500,blank=True, null=True)

#     def __str__(self) -> str:
#         return f'RESULTS -> {self.serviceDefinition}|{self.status}'

#     class Meta:
#         verbose_name='Service Results'
#         verbose_name_plural='Service Results'
