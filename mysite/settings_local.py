from .settings import *

import environ

env = environ.Env(DEBUG=(bool,True))

#환경변수 파일 읽어오기
environ.Env.read_env(
        env_file=os.path.join(BASE_DIR, '.env')
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}