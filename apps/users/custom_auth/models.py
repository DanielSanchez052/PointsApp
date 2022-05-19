from simple_history.models import HistoricalRecords
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)

class Auth(AbstractBaseUser, PermissionsMixin):
    CHOICE_STATUS = (
        (1,'INCOMPLETE'),
        (2,'COMPLETE'),
    )
    username = models.CharField(max_length = 255, unique = True)
    status = models.SmallIntegerField('status authentication',choices=CHOICE_STATUS, default=1)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    created_at = models.DateField('created at',auto_now_add=True,auto_now=False)
    modified_at = models.DateField('modified at',auto_now_add=False ,auto_now=True)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}|{self.is_active}'


class UserSession(models.Model):
    # Model to store the list of logged in users
    user = models.ForeignKey(Auth, on_delete=models.CASCADE, related_name='logged_in_user')
     # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username

