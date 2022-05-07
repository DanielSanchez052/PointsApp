import json

def extract_apps(apps, type):
        extracted_apps = set()
        for app in apps:
            app_splitted = app.split('.')
            if len(app_splitted) >= 2 and  app_splitted[1] == type:
                extracted_apps.add(app)
        return extracted_apps


def read_json(name=None,path=''): 
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