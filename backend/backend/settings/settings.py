import os
from .logger import LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'z_5%4!zuf9l+m9_c-0@7+=1*%n^qkfys&e-2#^u@^%vt5najzu'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'channels',
    'corsheaders',

    'rest_framework',
    'rest_framework.authtoken',
    'phonenumber_field',
    'versatileimagefield',

    'authenticate',
    'app.user',
    'app.order',
    'app.job',
    'app.setting',
    'app.generic'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'middleware.response.ResponseMiddleware'
]

ROOT_URLCONF = 'backend.urls'

AUTH_USER_MODEL = 'user.User'

WSGI_APPLICATION = 'backend.wsgi.application'

ASGI_APPLICATION = 'backend.asgi.application'

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
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
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

# 跨域
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ('*',)
CORS_ALLOW_METHODS = ('*',)

#rest socket
REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M",
    'ORDERING_PARAM': 'sorter',
    # 认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 自定义返回结果
    'DEFAULT_RENDERER_CLASSES': [
        'middleware.response.CustomJSONRenderer',
    ],
    # 过滤
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    # 定义限流类
    # 'DEFAULT_THROTTLE_CLASSES': (  
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ),
    # 定义限流速率，支持秒、分、时、天的限制
    'DEFAULT_THROTTLE_RATES': {   
        'anon': '100/day',
        'user': '100/day'
    },
    # 自定义分页
    'DEFAULT_PAGINATION_CLASS': 'middleware.pagination.CustomPagination',
}

AUTHENTICATION_BACKENDS = [
    'authenticate.backend.AuthBackend', 
]

# SMS Twilio
SENDSMS_BACKEND = 'core.sms.backends.twilio.SmsBackend'
SENDSMS_URL = "https://api.twilio.com/2010-04-01/Accounts/ACda91c280b2cd6511484f79ec3f3e03cd/Messages.json"
SENDSMS_ACCOUNT_SID = 'ACda91c280b2cd6511484f79ec3f3e03cd'
SENDSMS_AUTH_TOKEN = '6f00b28a9cdf341c31481a6f549b40da'
SENDSMS_FROM_NUMBER = '+15804564076'

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.eletec.ae'
EMAIL_USE_TLS = True
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'mobileapp@eletec.ae'
EMAIL_HOST_PASSWORD = 'eletec2015'
DEFAULT_FROM_EMAIL = 'eletec <mobileapp@eletec.ae>'

# 图片处理
VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'image_size': [
        ('full_size', 'url'),
        ('thumbnail', 'thumbnail__400x400'),
        ('samll', 'crop__640x360'),
        ('medium', 'crop__854x480'),
        ('large', 'crop__1280x720'),
    ],
    'app_size': [
        ('advertising', 'crop__1280x720'),
        ('banner', 'crop__854x480'),
    ]
}