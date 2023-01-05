import json

from celery import shared_task
from django.conf import settings
from django.utils.module_loading import import_string
from django.template.loader import render_to_string
from celery.utils.log import get_task_logger

from PointsApp.celery import app
from apps.users.notifications.models import Notification, NotificationType
from apps.core.tasks import send_async_email
from .strategy.context import Context

logger = get_task_logger(__name__)


@shared_task(name="execute notifications")
def run_notifications():
    notifications = Notification.objects.filter(
        notification_status=settings.NOTIFICATION_PENDING)

    for n in notifications:
        config = json.loads(n.config)
        notification_strategy = import_string(config["type"])

        logger.info(notification_strategy)

        context = Context(notification_strategy)

        context.execute_notification(config)
