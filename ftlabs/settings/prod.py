from ftlabs.settings.base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['user-activiti.herokuapp.com']

DATABASES = {
    'default':{}
}

db_from_env = dj_database_url.config(conn_max_age=600)

DATABASES['default'].update(db_from_env)

# Security settings

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True