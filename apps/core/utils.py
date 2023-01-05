import json
import importlib


def extract_apps(apps, type):
    extracted_apps = set()
    for app in apps:
        app_splitted = app.split('.')
        if len(app_splitted) >= 2 and app_splitted[1] == type:
            extracted_apps.add(app_splitted[-1])
    return extracted_apps


def read_json(name=None, path=''):
    data = {}
    try:
        if name == None:
            raise Exception
        with open(f'{path}{name}') as f:
            data = json.loads(f.read())
    except Exception as e:
        print(e)
    finally:
        return data


def get_request_ip(request):
    """
        Get IP from request user 
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
