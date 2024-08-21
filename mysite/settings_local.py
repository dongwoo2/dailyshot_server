from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'PORT': '3306',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}