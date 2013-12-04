# Django settings for rapoapp project.
import os

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

DEBUG =  True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': '/home/rapoadmin/public_html/devrapo/rapoapp/rapo.db',                      # Or path to database file if using sqlite3.
        'NAME': 'testdb',                      # Or path to database file if using sqlite3.
		#'OPTIONS': {
	    #         "init_command": "SET foreign_key_checks = 0;",
	    #} 
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.test.rapo.in']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Kolkata'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 3

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


USE_TZ = True
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/rapoadmin/public_html/devrapo/rapoapp/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = '/home/rapoadmin/public_html/rapoproject/rapoapp/static/'
STATIC_ROOT = '/home/rapoadmin/public_html/devrapo/rapoapp/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/media/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(PROJECT_ROOT,"static"),
	'/home/rapoadmin/public_html/devrapo/rapoapp/mystatic/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# Make this unique, and don't share it with anybody.
SECRET_KEY = '==!b72*)stdxd=)m24vab+_#rz2bwryitpq4-gk%b7k-c4gdpe'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
#    "mezzanine.core.middleware.UpdateCacheMiddleware",
#    "mezzanine.core.middleware.UpdateCacheMiddleware",
#    "django.contrib.sessions.middleware.SessionMiddleware",
#    "django.contrib.auth.middleware.AuthenticationMiddleware",
#    "django.middleware.common.CommonMiddleware",
#    "django.middleware.csrf.CsrfViewMiddleware",
#    "django.contrib.messages.middleware.MessageMiddleware",
#    "mezzanine.core.request.CurrentRequestMiddleware",
#    "mezzanine.core.middleware.RedirectFallbackMiddleware",
#    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
#    "mezzanine.core.middleware.TemplateForHostMiddleware",
#    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
#    "mezzanine.core.middleware.SitePermissionMiddleware",
#    # Uncomment the following if using any of the SSL settings:
#    # "mezzanine.core.middleware.SSLRedirectMiddleware",
#    "mezzanine.pages.middleware.PageMiddleware",
#    "mezzanine.core.middleware.FetchFromCacheMiddleware",
#)
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


#mez specific

#PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
#PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
#
#OPTIONAL_APPS = (
#    "debug_toolbar",
#    "django_extensions",
#    "compressor",
#    PACKAGE_NAME_FILEBROWSER,
#    PACKAGE_NAME_GRAPPELLI,
#)
# mez specific over



ROOT_URLCONF = 'rapoapp.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "templates"),
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
    'rapocore',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
# extra for mez
#    "django.contrib.redirects",
#    "django.contrib.sitemaps",
#    "mezzanine.boot",
#    "mezzanine.conf",
#    "mezzanine.core",
#    "mezzanine.generic",
#    "mezzanine.blog",
#    "mezzanine.forms",
#    "mezzanine.pages",
#    "mezzanine.galleries",
#    "mezzanine.twitter",
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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


LOGGING_LOG_SQL=True
#ADDING my GLOBALS SM
#FACEBOOK_API_KEY = '256281597846083'
#FACEBOOK_SECRET_KEY = '8feab4a8502cfeab289f973c9fedca9c'
#FACEBOOK_APP_NAME = "RAPO Database"
#FACEBOOK_INTERNAL = True
#FACEBOOK_CALLBACK_PATH = "/facebook/"



TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount'
)
AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)
#LOGIN_REDIRECT_URL = '/'
GEOIP_PATH = '/home/rapoadmin/public_html/devrapo/rapoapp/static/GeoIP.dat'
GEOIPV6_PATH = '/home/rapoadmin/public_html/devrapo/rapoapp/static/GeoIPv6.dat'
COMMENTS_APP = 'comments'

POSTMAN_AUTO_MODERATE_AS = True
