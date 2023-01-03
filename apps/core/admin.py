import functools
from django.contrib.admin import helpers
from django.template.response import TemplateResponse
from django.contrib.admin.utils import model_ngettext, get_deleted_objects


def intermediate_view(confirm_template="admin/action_confirmation.html", context={}):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(modeladmin, request, queryset):
            if request.POST.get("post"):
                return func(modeladmin, request, queryset)

            opts = modeladmin.model._meta
            app_label = opts.app_label
            objects_name = model_ngettext(queryset)
            (objects, model_count, perms_needed, protected) = get_deleted_objects(
                queryset, request, modeladmin.admin_site)
            context.update({
                **modeladmin.admin_site.each_context(request),
                "action": request.POST['action'],
                "queryset": queryset,
                "opts": opts,
                "objects_name": str(objects_name),
                "objects": [objects],
                "model_count": dict(model_count).items(),
                "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME
            })
            request.current_app = modeladmin.admin_site.name
            return TemplateResponse(request, confirm_template, context)

        wrapper.__name__ = func.__name__
        return wrapper
    return decorate


def require_confirmation(func):
    @functools.wraps(func)
    def wrapper(modeladmin, request, queryset):
        return intermediate_view(confirm_template="admin/action_confirmation.html", context={})(func)(modeladmin, request, queryset)
    return wrapper
