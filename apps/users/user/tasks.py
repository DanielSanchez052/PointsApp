import json
from django.conf import settings
from django.template.loader import render_to_string
from celery.utils.log import get_task_logger

from PointsApp.celery import app
from apps.users.notifications.models import Notification, NotificationType
from apps.core.tasks import send_async_email
from apps.users.custom_auth.models import Auth


logger = get_task_logger(__name__)


@app.task(name='Welcome user email')
def send_welcome_email(name, email, password, is_notification=False, context={}, *args, **kwargs):
    try:
        config_id = settings.WELCOME_EMAIL_ID_CONFIG
        configuration_email = json.loads(
            NotificationType.objects.filter(id=config_id).first().config)

        context.update({
            "name": name,
            "password": password
        })

        subject = configuration_email['subject'].format(name)

        html_message = render_to_string(
            configuration_email['template'], context)
        send_async_email.delay(
            subject,
            [email],
            '',
            html_message
        )
        if not is_notification:
            Notification.objects.create(
                auth_id=kwargs['user_id'],
                notification_status_id=settings.NOTIFICATION_COMPLETED,
                notification_type_id=settings.WELCOME_EMAIL_ID_CONFIG,
                name='welcome_email',
                result='SUCCESS',
                config=configuration_email)

        return 'Success'
    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]
