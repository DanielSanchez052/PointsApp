from django.conf import settings
from apps.core.utils import extract_apps


class ProductRouter:
    route_app_labels = {*(extract_apps(settings.LOCAL_APPS, 'products'))}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'product'
        return None


class UserRouter:
    route_app_labels = {
        *extract_apps(settings.LOCAL_APPS, 'users'),
        'auth', 'contenttypes', 'sessions', 'admin', 'django_rest_passwordreset', 'django_celery_beat', 'import_export_celery'
    }

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'user'
        return None
