from .base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mxr',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '139.9.236.103',
        'PORT': '5432',
    }
}

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ()
