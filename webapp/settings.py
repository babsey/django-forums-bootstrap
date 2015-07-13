"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from datetime import timedelta

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'crispy_forms',
    'accounts',
    'captcha',
    'webapp',
    'forum',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'webapp.urls'

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

WSGI_APPLICATION = 'webapp.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#  Accounts
# ===================
LOGIN_REDIRECT_URL = '/'

# The number of days an activation link is valid for
REGISTRATION_TIMEOUT_DAYS = 3
EMAIL_CHANGE_TIMEOUT_DAYS = 3

# Period of time between two email requests for individual user
# (for now using for password reset only)
EMAIL_REQUEST_DELAY = timedelta(minutes=30)

# Community page
ACCOUNTS_PER_PAGE = 20


#  Forum
# ===================
TOPICS_PER_PAGE = 10
POSTS_PER_PAGE = 10
SUBSCRIPTIONS_PER_PAGE = 15

POPULAR_TOPICS_PERIOD = timedelta(days=7)
POPULAR_TOPICS_COUNT = 7

NEW_TOPICS_COUNT = 7

TOPIC_PAGINATION_LEFT_TAIL = 3
TOPIC_PAGINATION_RIGHT_TAIL = 5

GLUE_MESSAGE_TIMEOUT = 10*60
GLUE_MESSAGE = u'\n\n[color=#BBBBBB][small]Added %s[/small] later[/color]\n%s'

FORUM_UNREAD_DEPTH = 100

FORUM_FEED_ITEMS_COUNT = 30

BBMARKUP_EXTRA_RULES = [
    {'pattern': r'\[hidden\](.*?)\[/hidden\]', 'repl': ur'<div class="hidden-header">Hidden text</div><div class="hidden-text" style="display: none">\1</div>'},
    {'pattern': r'\[hidden title=(.*?)\](.*?)\[/hidden\]', 'repl': ur'<div class="hidden-header">\1</div><div class="hidden-text" style="display: none">\2</div>'},
    {'pattern': r'\[video\]http://www\.youtube\.com/watch\?v=([a-z\d_-]+)\[/video\]', 'repl': r'<div class="video"><iframe class="youtube-player" type="text/html" width="748" height="455" src="http://www.youtube.com/embed/\1" frameborder="0"></iframe></div>'},
]


#  Pagination
# ===================

# 1 2 ... 6 7 [8] 9 10 ... 91 92
# |_|     |_|     |__|     |___|
# tail     ^padding^        tail
PAGINATION_PADDING = 3
PAGINATION_TAIL = 2


# Import local settings depending on running environment
# See local_settings.sample for example
try:
    from local_settings import *
except ImportError:
    pass
