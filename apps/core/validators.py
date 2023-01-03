from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from rest_framework.validators import qs_exists, qs_filter


@deconstructible
class UniqueInValidator:
    message = "%(field_label)s  must be unique in %(model_name)s model"
    code = 'unique'
    lookup = 'exact'

    def __init__(self, model, field_name, queryset=None):
        self.model = model
        self.field_name = field_name
        self.queryset = self.model.objects.all()

        # if message:
        #     self.message = message

        if queryset:
            self.queryset = queryset

    def __call__(self, value):
        cleaned = self.clean(value)
        params = {"field_label": self.field_name,
                  "model_name": self.model._meta.model_name}
        queryset = self.filter_queryset(cleaned, self.field_name)
        if qs_exists(queryset):
            self.message = self.message.format(
                field=self.field_name, model=self.model)

            raise ValidationError(message=self.message,
                                  code='unique', params=params)

    def clean(self, x):
        return x

    def filter_queryset(self, value, field_name):
        filter = {'%s__%s' % (field_name, self.lookup): value}
        return qs_filter(self.queryset, **filter)
