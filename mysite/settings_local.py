from .settings import *

import environ

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, 'local.env'))



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'PORT': '3306',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}