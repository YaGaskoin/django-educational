from .base import *
DEBUG = False
ADMINS = (
('gaskoin', 'dchierntsov@mail.ru'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'daniloka',
    }
}