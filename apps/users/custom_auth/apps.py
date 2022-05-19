from django.apps import AppConfig


class CustomAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users.custom_auth'

    def ready(self):
        import apps.users.custom_auth.signals