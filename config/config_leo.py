import os

debug = True

database = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emailapi',
        'USER': 'emailapi',
        'PASSWORD': 'RfvDX64VVJhU',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

STATIC_ROOT = '/home/kyalma/source/email_api/static/'

SECURE_PROXY_SSL_HEADER = None

SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False
