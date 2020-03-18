from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['*']

#Channels
redis_host = os.environ.get('REDIS_HOST', 'localhost')

# Channel layer definitions
# http://channels.readthedocs.io/en/latest/topics/channel_layers.html
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(redis_host, 6379)],
        },
    },
}

# Twilio
SENDSMS_URL = "https://api.twilio.com/2010-04-01/Accounts/ACda91c280b2cd6511484f79ec3f3e03cd/Messages.json"
SENDSMS_ACCOUNT_SID = 'ACda91c280b2cd6511484f79ec3f3e03cd'
SENDSMS_AUTH_TOKEN = '6f00b28a9cdf341c31481a6f549b40da'
SENDSMS_FROM_NUMBER = '+15804564076'