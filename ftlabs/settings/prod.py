from ftlabs.settings.base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['user-activiti.herokuapp.com']

DATABASES = {
    'default':{}
}

db_from_env = dj_database_url.config(conn_max_age=600)

DATABASES['default'].update(db_from_env)