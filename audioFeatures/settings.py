# Django settings for audioFeatures project.
import os
import sys
import django.conf.global_settings as DEFAULT_SETTINGS

PROJECT_DIR = os.path.dirname(__file__)
TEMPLATE_DIRS = os.path.join(PROJECT_DIR, 'templates')
sys.path.insert(0, os.path.join(PROJECT_DIR, 'apps'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('admin', 'alex@againstyou.net'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, 'data.db'),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# media deliver
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

# static files (application js/img etc)
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'site-static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=v&991ik4m2&h2(9jt8f0obb_ahmbp)4up0a0&+qj*w38nn&7o'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'audioFeatures.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'audioFeatures.wsgi.application'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    #...#
    'django.core.context_processors.request',
    #...#
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django_extensions',
    'audioFeatures',
    'af_documentation',
    'audio',
    'audio_processor',
    'mptt',
    'inplaceeditform',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

INPLACEEDIT_EDIT_EMPTY_VALUE = 'Double click to edit'
INPLACEEDIT_AUTO_SAVE = True
INPLACEEDIT_EVENT = "dblclick"
INPLACEEDIT_DISABLE_CLICK = True  # For inplace edit text into a link tag
INPLACEEDIT_EDIT_MESSAGE_TRANSLATION = 'Write a translation' # transmeta option
INPLACEEDIT_SUCCESS_TEXT = 'Successfully saved'
INPLACEEDIT_UNSAVED_TEXT = 'You have unsaved changes'
INPLACE_ENABLE_CLASS = 'enable'
#DEFAULT_INPLACE_EDIT_OPTIONS = {} # dictionnary of the optionals parameters that the templatetag can receive to change its behavior (see the Advanced usage section)
#DEFAULT_INPLACE_EDIT_OPTIONS_ONE_BY_ONE = True # modify the behavior of the DEFAULT_INPLACE_EDIT_OPTIONS usage, if True then it use the default values not specified in your template, if False it uses these options only when the dictionnary is empty (when you do put any options in your template)
#ADAPTOR_INPLACEEDIT_EDIT = 'app_name.perms.MyAdaptorEditInline' # Explain in Permission Adaptor API
#ADAPTOR_INPLACEEDIT = {'myadaptor': 'app_name.fields.MyAdaptor'} # Explain in Adaptor API
INPLACE_GET_FIELD_URL = None # to change the url where django-inplaceedit use to get a field
INPLACE_SAVE_URL = None # to change the url where django-inplaceedit use to save a field
