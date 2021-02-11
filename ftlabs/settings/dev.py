from ftlabs.settings.base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

try:
    from ftlabs.settings.local import *

except ImportError:
    print("local environment setup is not done please complete it")