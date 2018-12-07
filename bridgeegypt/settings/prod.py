from bridgeegypt.settings.base import *

# override base.py setting here

DEBUG=False
ALLOWED_HOSTS=['bridgeegypt.herokuapp.com', 'www.bridgeegypt.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# add this
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'bridgegypt',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD':'',
#         'OPTIONS':{'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
# }
# }


CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True


try:
    from bridgeegypt.settings.local import *

except:
    pass