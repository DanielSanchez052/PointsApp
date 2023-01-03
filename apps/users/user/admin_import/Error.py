from django.conf import settings


class CustomError:
    def __init__(self, error, traceback=None, row=None):
        debug = getattr(settings, 'DEBUG', False)
        self.error = f"Error: {error} Line: {row['import_id']}"
        self.traceback = '' if not debug else traceback
        self.row = row
