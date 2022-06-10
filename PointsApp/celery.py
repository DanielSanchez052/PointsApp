import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PointsApp.conf.local')

app = Celery('PointsApp')
app.config_from_object('django.conf:settings', namespace= 'CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def default_task(self):
    print(f'Request: {self.request}')

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'apps.core.tasks.test_task',
#         'schedule': 60.0,
#         'args': ()
#     },
# }