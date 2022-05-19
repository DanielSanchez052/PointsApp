from django.contrib.auth import user_logged_in, user_logged_out
from django.db.models.signals import post_delete
from django.contrib.sessions.models import Session
from django.dispatch import receiver
from .models import UserSession, Auth
from django.conf import settings
from django.contrib.sessions.models import Session

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    UserSession.objects.get_or_create(user=kwargs.get('user'), session_key=request.session.session_key) 
    number_sessions = settings.LIMIT_NUMBER_SESSIONS if settings.LIMIT_NUMBER_SESSIONS and settings.LIMIT_NUMBER_SESSIONS != 0 else 1 
    limit_sessions = settings.LIMIT_SESSIONS if settings.LIMIT_SESSIONS else True
    
    if limit_sessions:
        try:
            user_logins = UserSession.objects.filter(user=kwargs.get('user')).exclude(session_key=request.session.session_key).values('session_key')
            if len(user_logins) < number_sessions:  
                return 
            sessions = [ login.get('session_key') for login in user_logins ]
            open_session = Session.objects.filter(session_key__in=sessions).order_by('-expire_date')
            if open_session.count() >= number_sessions:
                session_delete = [ session.session_key for session in open_session]
                close_sessions = session_delete[:(open_session.count() - limit_sessions)+1]
                Session.objects.filter(pk__in=close_sessions).delete()
        except Auth.DoesNotExist as e:
            pass




@receiver(post_delete, sender=Session)
def on_user_logged_out(sender, instance,**kwargs):
    UserSession.objects.filter(session_key=instance.session_key).delete()
