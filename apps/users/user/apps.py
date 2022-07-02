from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users.user'

    def ready(self):
        import apps.users.user.signals