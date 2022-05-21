from PointsApp.conf.base import *
from PointsApp.utils import read_json
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', default=True)

ALLOWED_HOSTS = ['0.0.0.0','localhost','127.0.0.1', os.environ.get('SERVER', default='127.0.0.1')]

LIMIT_SESSIONS= True
LIMIT_NUMBER_SESSIONS= 1

CSRF_TRUSTED_ORIGINS = ["http://localhost:85","http://127.0.0.1:85"]
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASE_ROUTERS = ['routers.db_routers.UserRouter','routers.db_routers.ProductRouter',]


DATABASES = read_json('db_conection_dev.json',os.path.join(BASE_DIR, 'conf/db_conection/'))

INTERNAL_IPS = ['127.0.0.1','0.0.0.0']
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
}