from PointsApp.conf.base import *
from PointsApp.utils import read_json


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda f: [s.strip() for s in f.split(',')])

##Authentication config
LIMIT_SESSIONS= config('LIMIT_SESSIONS', cast=bool)
LIMIT_NUMBER_SESSIONS= config('LIMIT_NUMBER_SESSIONS', cast=int)

USER_LOCKED_MINUTES= config('USER_LOCKED_MINUTES', cast=int)
USER_LOCKED_ATTEMPTS= config('USER_LOCKED_ATTEMPTS', cast=int)

DJANGO_REST_PASSWORDRESET_IP_ADDRESS_HEADER = 'HTTP_X_FORWARDED_FOR'
DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME = 2
PASSWORD_RESET_FORM_URL='http://localhost:85/auth/password_reset/confirm/'

##CSRF config
CSRF_TRUSTED_ORIGINS = ["http://localhost:85","http://127.0.0.1:85"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


##Databases Config
DATABASE_ROUTERS = ['routers.db_routers.UserRouter','routers.db_routers.ProductRouter',]

DATABASES = read_json('db_conection_dev.json',os.path.join(BASE_DIR, 'conf/db_conection/'))

##Debug Tools Config
INTERNAL_IPS = ['127.0.0.1','0.0.0.0']
if DEBUG:
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
    }