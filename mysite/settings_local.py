from .settings import *
import os
import environ

# BASE_DIR 정의
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 환경 변수 설정
env = environ.Env()
env.read_env(os.path.join(os.path.dirname(__file__), 'local.env'))

# 데이터베이스 설정
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # SQLite의 경우 NAME만 필요합니다.
    }
}
