def resourceUser():
    from apps.users.user.admin_import.user_import import LoadUsersResource
    return LoadUsersResource


IMPORT_EXPORT_CELERY_MODELS = {
    "LoadUsers": {
        'app_label': 'user',
        'model_name': 'LoadUsers',
        'resource': resourceUser
    },
}
