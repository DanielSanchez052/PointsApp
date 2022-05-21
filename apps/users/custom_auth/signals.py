from django.contrib.auth import user_logged_in
from django.db.models.signals import post_delete
from django.db.models import Q
from django.contrib.sessions.models import Session
from django.dispatch import receiver
from django.conf import settings

from .models import UserSession


@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    try:
    #insert register for sessions control
        UserSession.objects.create(user=kwargs.get('user'), session_key=request.session.session_key)

        number_sessions = settings.LIMIT_NUMBER_SESSIONS if settings.LIMIT_NUMBER_SESSIONS and settings.LIMIT_NUMBER_SESSIONS != 0 else 1 
        limit_sessions = settings.LIMIT_SESSIONS if settings.LIMIT_SESSIONS else True

        if limit_sessions:
            
            #sessions registered
            user_logins = list(UserSession.objects.filter(Q(user=kwargs.get('user')) & ~Q(session_key=request.session.session_key))
                                                    .values_list('session_key', flat=True))
            #sessions opened
            open_session = list(Session.objects.filter(session_key__in=user_logins).order_by('expire_date')
                                                .values_list('session_key', flat=True))
            if len(open_session) < number_sessions:  
                return 
            close_sessions = open_session[:(len(open_session) - number_sessions)+1]
            Session.objects.filter(pk__in=close_sessions).delete()

    except Exception as e:
        print(e.args[0])
        pass


@receiver(post_delete, sender=Session)
def on_user_logged_out(sender, instance,**kwargs):
    UserSession.objects.filter(session_key=instance.session_key).delete()


# @receiver(user_logged_in)
# def on_user_logged_in(sender, request, **kwargs):
#     #insert register for sessions control
#     UserSession.objects.create(user=kwargs.get('user'), session_key=request.session.session_key) 

#     number_sessions = settings.LIMIT_NUMBER_SESSIONS if settings.LIMIT_NUMBER_SESSIONS and settings.LIMIT_NUMBER_SESSIONS != 0 else 1 
#     limit_sessions = settings.LIMIT_SESSIONS if settings.LIMIT_SESSIONS else True

#     if limit_sessions:
#         try:
#             #sessions registered
#             user_logins = list(list(UserSession.objects.filter(Q(user=kwargs.get('user')) & ~Q(session_key=request.session.session_key))
#                                                     .values_list('session_key', flat=True)))
            
#             if len(user_logins) < number_sessions:  
#                 return 

#             #sessions opened
#             open_session = list(Session.objects.filter(session_key__in=user_logins).order_by('expire_date')
#                                                 .values_list('session_key', flat=True))

#             if len(open_session) >= number_sessions:
#                 close_sessions = user_logins[:(len(open_session) - number_sessions)+1]
#                 Session.objects.filter(pk__in=close_sessions).delete()
#         except Exception as e:
#             print(e.args)
#             pass
