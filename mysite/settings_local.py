from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'USER': env('MYSQL_USER_NAME',default='root'),
        'PASSWORD': 'MYSQL_PASSWORD',
        'PORT': '3306',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}