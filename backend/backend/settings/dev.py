from .settings import *

DEBUG = True

SENDSMS_BACKEND = 'service.sms.backends.console.SmsBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'