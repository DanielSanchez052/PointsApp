import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PointsApp.conf.local')

app = Celery('PointsApp')
app.config_from_object('django.conf:settings', namespace= 'CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def default_task(self):
    print(f'Request: {self.request}')