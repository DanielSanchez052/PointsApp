from import_export import resources

from apps.users.user.models import LoadUsers
from .Error import CustomError


class LoadUsersResource(resources.ModelResource):
    class Meta:
        model = LoadUsers
        import_id_fields = ('email',)
        exclude = ('id', 'status')

    @classmethod
    def get_error_result_class(self):
        """
        Returns the class used to store an error resulting from an import.
        """
        return CustomError

    def import_data(self, dataset, dry_run=False, raise_errors=False, **kwargs):
        return super().import_data(dataset, dry_run, raise_errors, **kwargs)
