import uuid
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
    username = models.CharField(max_length = 255, unique = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    created_at = models.DateField('created at',auto_now_add=True,auto_now=False)
    modified_at = models.DateField('modified at',auto_now_add=False ,auto_now=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Auth'
        verbose_name_plural = 'Auth'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}|{self.is_active}'