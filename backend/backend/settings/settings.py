import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'z_5%4!zuf9l+m9_c-0@7+=1*%n^qkfys&e-2#^u@^%vt5najzu'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'rest_framework_jwt',
    'rest_framework.authtoken',
    'phonenumber_field',

    'app.user',
    'app.order',
    'app.job',
    'app.contract',

    'auth.phone',
    'service.sms'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

AUTH_USER_MODEL = 'user.User'

WSGI_APPLICATION = 'backend.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dubai'

USE_I18N = True

USE_L10N = False

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'media')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': (  # 定义限流类
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {   # 定义限流速率，支持秒、分、时、天的限制
        'anon': '1/m',
        'user': '1/m'
    }
}

AUTHENTICATION_BACKENDS = [
    'auth.phone.backends.phone_backend.PhoneBackend',
    'django.contrib.auth.backends.ModelBackend'
]

SENDSMS_BACKEND = 'service.sms.backend.console.SmsBackend'
SENDSMS_FROM_NUMBER = '+15005550006'

TWILIO_URL = "https://api.twilio.com/2010-04-01/Accounts/AC3d23045bf1213f916b7c082028412e53/Messages.json"
TWILIO_ACCOUNT_SID = 'AC3d23045bf1213f916b7c082028412e53'
TWILIO_AUTH_TOKEN = 'c54b1663080a2dae8eb0c7cf71bccdcf'
TWILIO_FROM_NUMBER = '+15005550006'