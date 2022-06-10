from django.contrib.auth import user_logged_in, user_login_failed
from django.db.models.signals import post_delete
from django.contrib.sessions.models import Session
from django.dispatch import receiver
from django.conf import settings
from django.template.loader import render_to_string

from django_rest_passwordreset.signals import reset_password_token_created

from .models import UserSession, Auth, IpLocked
from apps.core.utils import get_request_ip
from apps.core.tasks import send_async_email
from .tasks import valid_user_login

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    #print(type(kwargs.get('user').id))
    valid_user_login.delay(kwargs.get('user').id, request.session.session_key)

@receiver(user_login_failed)
def on_login_fail(sender, request,**kwags):
    username = request.data['username']
    request_ip = get_request_ip(request)

    try:
        user = Auth.objects.get(username=username)
         
        if user.attempts < settings.USER_LOCKED_ATTEMPTS:
            user.attempts += 1
            user.save()

        if user.attempts >= settings.USER_LOCKED_ATTEMPTS:
            ip_locked = IpLocked.objects.lock_ip(request_ip)

    except Auth.DoesNotExist:
        print('No Existe')

@receiver(post_delete, sender=Session)
def on_user_logged_out(sender, instance,**kwargs):
    UserSession.objects.filter(session_key=instance.session_key).delete()

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """

    # end an e-mail to the users
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            settings.PASSWORD_RESET_FORM_URL,
            reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    send_async_email.delay(
        "Password Reset for {title}".format(title="Some website title"),
        [reset_password_token.user.email],
        email_plaintext_message,
        email_html_message
    )