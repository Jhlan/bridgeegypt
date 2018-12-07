from bridgeegypt.settings.base import *

# override base.py setting here

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bridgegypt',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD':'',
        'OPTIONS':{'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
}
}

try:
    from bridgeegypt.settings.local import *

except:
    pass
