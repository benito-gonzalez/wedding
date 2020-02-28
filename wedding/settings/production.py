from wedding.settings.common import *

ALLOWED_HOSTS = ['54.38.158.6', 'www.eugeybeni.com', 'eugeybeni.com']

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Production configs
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

PREPEND_WWW = True
