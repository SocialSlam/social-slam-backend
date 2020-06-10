from settings.settings_dev import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'social_slam_db',
        'USER': 'social_slam_admin',
        'PASSWORD': 'social_slamming_2020',
        'HOST': 'db',
        'PORT': '5432',
    }
}