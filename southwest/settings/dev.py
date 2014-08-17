DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'southwest',
        'USER': 'vagrant',
        'PASSWORD': 'acer83',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}