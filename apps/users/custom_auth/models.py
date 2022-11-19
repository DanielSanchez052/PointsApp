import uuid
from datetime import timedelta

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.conf import settings
from django.contrib.sessions.models import Session

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email,password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

class Auth(AbstractBaseUser, PermissionsMixin):
    """
    store user information for authenticatation user
      * username
      * password
      * email
      * is_active
      * is_staff
      * status
    """

    CHOICE_STATUS = (
        (1,'INCOMPLETE'),
        (2,'COMPLETE'),
    )
    email = models.CharField('email', max_length=250, unique=True, blank=True)
    username = models.CharField(max_length=255, unique = True)
    status = models.SmallIntegerField('status authentication', choices=CHOICE_STATUS, default=1)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateField('created at', auto_now_add=True, auto_now=False)
    modified_at = models.DateField('modified at', auto_now_add=False, auto_now=True)
    attempts = models.SmallIntegerField('attempts to block', default=0)
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.username}|{self.is_active}'


class UserSessionManager(models.Manager):
    def get_sessions_by_user(self, user):
        user_logins = self.filter(user=user).values('session_key')
        #sessions opened
        return list(Session.objects.filter(session_key__in=user_logins).order_by('expire_date').values_list('session_key', flat=True))
        
class UserSession(models.Model):
    """
    store user session information
      * user
      * session_key
    """

    # Model to store the list of logged in users
    user = models.ForeignKey(Auth, on_delete=models.CASCADE, related_name='logged_in_user')
     # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)
    # session_key = models.ForeignKey(Session, on_delete= models.CASCADE, related_name='user_session')

    objects = UserSessionManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'session_key'], name="%(app_label)s_%(class)s_unique")
        ]

    def __str__(self):
        return self.user.username

class IpLockedManager(models.Manager):
    
    def is_locked(self, ip):
        now = timezone.now() - timedelta(minutes=settings.USER_LOCKED_MINUTES)
        return self.filter(models.Q(ip=ip) & models.Q(created_at__gte=now)).exists()

    def lock_ip(self, ip):
        ip_locked = None

        if not self.is_locked(ip):
            ip_locked = self.model(
                ip=ip,
                created_at = timezone.now()
            )

            ip_locked.save(using=self.db)
        
        return ip_locked if ip_locked else f'Ip address {ip} already is locked'

class IpLocked(models.Model):
    """
    store locked IPs
      * id
      * ip
      * created_at 
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    ip = models.CharField('Ip locked', max_length=45)
    #unlocked_date = models.DateField('locked_date',auto_now_add=False,auto_now=False, default=timezone.now() + timedelta(minutes=settings.USER_LOCKED_MINUTES|15))
    created_at = models.DateTimeField('created at')

    objects= IpLockedManager()

    class Meta:
        verbose_name = 'IpLocked'
        verbose_name_plural = 'IpLocked'

    def __str__(self):
        return f'{self.ip}|{self.created_at}'
        
