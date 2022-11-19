from django.conf import settings
from django.contrib.sessions.models import Session

from celery import shared_task
from celery.utils.log import get_task_logger

from .models import UserSession,Auth

logger = get_task_logger(__name__)

@shared_task(name=' Validate user login')
def valid_user_login(user_id, session_key):
    """
    Validate if sessions are limited and number of active sessions 
    
    :param user_id: user_id for check your sessions 
    :param session_key: new session_key gerated for user 
    """
    try:
        number_sessions = settings.LIMIT_NUMBER_SESSIONS if settings.LIMIT_NUMBER_SESSIONS and settings.LIMIT_NUMBER_SESSIONS != 0 else 1 
        limit_sessions = settings.LIMIT_SESSIONS if settings.LIMIT_SESSIONS else True

        user = Auth.objects.get(id=user_id)

        if limit_sessions:
            open_session = UserSession.objects.get_sessions_by_user(user)
            
            if not len(open_session) < number_sessions:  
                #deauthenticate number of users defined by oldest sessions  
                close_sessions = open_session[:(len(open_session) - number_sessions)+1]
                Session.objects.filter(pk__in=close_sessions).delete()
        return 'Success'
    except Exception as e:
        logger.info(e.args[0])
        return e.args[0]

    finally:
        #insert register for sessions control
        UserSession.objects.get_or_create(user=user, session_key=session_key)



    