from datetime import timedelta
import os
import djcelery
from unipath import Path


djcelery.setup_loader()
PROJECT_DIR = os.path.dirname(__file__)

ADMINS = (
     ('Christopher Johnson', 'christopher.johnson@wikimedia.de'),
)

# Django settings for scrumbugz project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

BUGMAIL_HOST= 'scrumbugz.pmtpa.wmflabs'
BUGMAIL_USER= '*****'
BUGMAIL_PASS= '*****'
BUGZILLA_SHOW_URL= 'http://wmde-bugs.wmflabs.org/show_bug.cgi?'
BUGZILLA_API_URL= 'http://scrumbugz.pmtpa.wmflabs/xmlrpc.cgi'
BUGZILLA_SEARCH_URL= 'http://scrumbugz.pmtpa.wmflabs/query.cgi'
BUGZILLA_USER = 'christopher.johnson@wikimedia.de'
BUGZILLA_PASS = '*****'
SITE_URL = 'http://scrum.pmtpa.wmflabs'


SECRET_KEY = "shhhhhh"
INTERNAL_IPS = (
    '127.0.0.1',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'scrumbugs',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '*****',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MANAGERS = ADMINS

BUGZILLA_BASE_URL = 'http://scrumbugz.pmtpa.wmflabs'
CACHE_BUGS_FOR = 4  # hours

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

CONTEXT_SETTINGS = (
    'CACHE_BUGS_FOR',
    'DEBUG',
    'ENABLE_GA',
    'BUGZILLA_SHOW_URL',
    'BUGZILLA_FILE_URL',
    'BUGZILLA_ATTACHMENT_URL',
    'PROD_MODE',
)

# http://packages.python.org/Markdown/extensions/index.html
MARKDOWN_EXTENSIONS = [
    'fenced_code',
    'tables',
    'smart_strong',
    'sane_lists',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
	'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 500,
        'BINARY': True,
        'OPTIONS': {
            'tcp_nodelay': True,
            'ketama': True,
        },
    },
}
PYLIBMC_MIN_COMPRESS_LEN = 150 * 1024
CACHE_COUNT_TIMEOUT = 10  # seconds, not too long.

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
USE_TZ = True


MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, "static_root")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(os.path.join(PROJECT_DIR, "static")),
)

JINGO_EXCLUDE_APPS = (
    'admin',
    'auth',
    'context_processors',  # needed for django tests
    'debug_toolbar',
    'floppyforms',
    'registration',  # needed for django tests
)

JINJA_CONFIG = {
    'extensions': (
        'jinja2.ext.do',
        'jinja2.ext.loopcontrols',
        'jinja2.ext.with_',
    ),
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
#    'johnny.middleware.LocalStoreClearMiddleware',
#    'johnny.middleware.QueryCacheMiddleware',
    'middleware.EnforceHostnameMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates")

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'cronjobs',
    'bootstrap',
    'floppyforms',
   'djcelery',
    'scrum',
    'bugmail',
    'bugzilla',
    'south',
    'django_nose',
    'django_browserid',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'context_processors.context_settings',
    'scrum.context_processors.projects_and_teams',
    'django_browserid.context_processors.browserid_form',
)

AUTHENTICATION_BACKENDS = (
    'django_browserid.auth.BrowserIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)
LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL_FAILURE = '/'
LOGIN_URL = LOGOUT_URL = '/'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--logging-clear-handlers',
]

# Celery
CELERY_IMPORTS = ('bugmail')
#BROKER_URL = "amqp://scrumbugz:scrumbugz@localhost:5672//"
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672   # default RabbitMQ listening port
BROKER_USER = "scrumbugz"
BROKER_PASSWORD = "scrumbugz"
BROKER_VHOST = "scrumbugz"
CELERY_RESULT_BACKEND = "amqp"
CELERY_DISABLE_RATE_LIMITS = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_TASK_RESULT_EXPIRES = 60
#CELERY_TIMEZONE = 'Europe/Berlin'
CELERYD_CONCURRENCY = 4
CELERYBEAT_SCHEDULE = {
    'get-bugmails': {
        'task': 'get_bugmails',
        'schedule': timedelta(minutes=1),
    },
#    'update_product': {
#        'task': 'update_product',
#        'schedule': timedelta(minutes=1),
#    },
#    'update_bugs': {
#        'task': 'update_bugs',
#        'schedule': timedelta(minutes=1),
#    },
#    'update_sprint_data': {
#        'task': 'update_sprint_data',
#        'schedule': timedelta(minutes=1),
#    },
    'clean-bugmails': {
        'task': 'clean_bugmail_log',
        'schedule': timedelta(days=5),
    },
}

BUG_OPEN_STATUSES = [
    'UNCONFIRMED',
    'CONFIRMED',
    'ASSIGNED',
    'REOPENED',
    'READY',
    'NEW',
]
BUG_CLOSED_STATUSES = [
    'RESOLVED',
    'VERIFIED',
    'CLOSED',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/usr/local/django/logs/django.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },  
        'request_handler': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': '/usr/local/django/logs/django_request.log',
                'maxBytes': 1024*1024*5, # 5 MB
                'backupCount': 5,
                'formatter':'standard',
        },
	'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
	},
    },
    'loggers': {

        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
            'django_browserid': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}
