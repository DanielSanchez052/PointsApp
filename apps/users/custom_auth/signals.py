from re import T
from django.contrib.auth import user_logged_in, user_login_failed
from django.db.models.signals import post_delete
from django.contrib.sessions.models import Session
from django.dispatch import receiver
from django.conf import settings

from .models import UserSession, Auth, IpLocked
from apps.core.utils import get_request_ip

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    try:
        number_sessions = settings.LIMIT_NUMBER_SESSIONS if settings.LIMIT_NUMBER_SESSIONS and settings.LIMIT_NUMBER_SESSIONS != 0 else 1 
        limit_sessions = settings.LIMIT_SESSIONS if settings.LIMIT_SESSIONS else True

        if limit_sessions:
            open_session = UserSession.objects.get_sessions_by_user(kwargs.get('user'))
            
            if not len(open_session) < number_sessions:  
                close_sessions = open_session[:(len(open_session) - number_sessions)+1]
                Session.objects.filter(pk__in=close_sessions).delete()

    except Exception as e:
        print(e.args[0])
        pass

    finally:
        #insert register for sessions control
        UserSession.objects.get_or_create(user=kwargs.get('user'), session_key=request.session.session_key)

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


