import logging
from celery.utils.log import get_task_logger

from django.core.exceptions import ValidationError
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export.results import RowResult
from collections import OrderedDict

from apps.users.user.models import LoadUsers, City, IdentificationType
from .Error import CustomError

logger = logging.getLogger(__name__)
log = get_task_logger(__name__)


class ValidateInWidget(ForeignKeyWidget):
    def get_queryset(self, value, row, *args, **kwargs):
        return self.model.objects.all()

    def render(self, value, obj=None):
        return value


class LoadUsersResource(resources.ModelResource):
    identification_type = resources.Field(
        column_name='identification_type', attribute='identification_type',
        widget=ValidateInWidget(IdentificationType, field='name'))

    city = resources.Field(
        column_name='city', attribute='city',
        widget=ValidateInWidget(City, field='name'))

    class Meta:
        model = LoadUsers
        clean_model_instances = True
        skip_unchanged = True
        report_skipped = True
        raise_errors = False
        import_id_fields = ('import_id',)
        import_id_field = 'import_id'
        fields = ('import_id', 'email', 'username', 'identification_type', 'identification',
                  'city', 'name', 'last_name', 'phone', 'phone2', 'address', 'postal_code')
        # new config options
        skip_error_rows = True
        skip_invalid_rows = True

    @classmethod
    def get_error_result_class(self):
        """
        Returns the class used to store an error resulting from an import.
        """
        return CustomError

    def import_row(self, row, instance_loader, **kwargs):

        import_result = super(LoadUsersResource, self).import_row(
            row, instance_loader, **kwargs)

        if self._meta.skip_error_rows:
            self.skip_error_rows(import_result, row)

        if self._meta.skip_invalid_rows:
            self.skip_invalid_rows(import_result, row)

        return import_result

    def skip_invalid_rows(self, import_result, row, **kwargs):
        # skip invalid lines and add errir in new column
        try:
            if import_result.import_type == RowResult.IMPORT_TYPE_INVALID:
                # Add names to result diff
                import_result.diff = [
                    str(row.get(name, '')) for name in self.get_field_names()
                ]
                # Add Errors in new column
                import_result.diff.append("Errors: {}".format(
                    [*import_result.validation_error]))
                # clean validation error
                import_result.validation_error = []
                # Skip column
                import_result.import_type = RowResult.IMPORT_TYPE_SKIP
        except Exception as e:
            print(e)

    def skip_error_rows(self, import_result, row, **kwargs):
        # skip invalid lines and add errir in new column
        try:
            if import_result.import_type == RowResult.IMPORT_TYPE_ERROR:
                # Add names to result diff
                import_result.diff = [
                    str(row.get(name, '')) for name in self.get_field_names()
                ]
                import_result.diff.append('Errors: {}'.format(
                    [err.error for err in import_result.errors]))
                # clear errors and mark the record to skip
                import_result.errors = []
                import_result.import_type = RowResult.IMPORT_TYPE_SKIP

        except Exception as e:
            print(e)

    def get_field_names(self):
        names = []
        for field in self.get_fields():
            names.append(self.get_field_name(field))
        return names
