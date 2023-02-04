
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'postgres',
        'PASSWORD': 'quanghiep0905',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = []

CSRF_TRUSTED_ORIGINS = ['localhost']

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8001',
    'http://localhost:8000',
    'http://localhost:3000',
    'http://127.0.0.1',
    'http://127.0.0.1:8001',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'http://localhost',
)