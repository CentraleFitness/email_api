debug = False

database = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emailapi',
        'USER': 'emailapi',
        'PASSWORD': 'qaxLUfVy',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

STATIC_ROOT = '/var/www/email_api/static/'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True
