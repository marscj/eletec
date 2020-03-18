from .settings import *

DEBUG = True

SENDSMS_BACKEND = 'core.sms.backends.console.SmsBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# channel for websocket 
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}