from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Twilio
SENDSMS_URL = "https://api.twilio.com/2010-04-01/Accounts/ACcf794b0edd7c3f5a2d5be559eef0e254/Messages.json"
SENDSMS_ACCOUNT_SID = 'ACcf794b0edd7c3f5a2d5be559eef0e254'
SENDSMS_AUTH_TOKEN = 'c3c8de0672d273e483e1e2f493c06da8'
SENDSMS_FROM_NUMBER = '+13473086886'