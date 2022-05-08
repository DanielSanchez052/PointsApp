from email.mime import base
from PointsApp.conf.base import *
from PointsApp.utils import read_json
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', default=True)

ALLOWED_HOSTS = ['0.0.0.0','localhost', 'localhost', '127.0.0.1', os.environ.get('SERVER', default='127.0.0.1')]

CSRF_TRUSTED_ORIGINS = ["http://localhost:85","http://127.0.0.1"]
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = read_json('db_conection_dev.json',os.path.join(BASE_DIR, 'conf/db_conection/'))

DATABASE_ROUTERS = [
    'PointsApp.conf.database_router.user_router.UserRouter',
    'PointsApp.conf.database_router.product_router.ProductRouter']
