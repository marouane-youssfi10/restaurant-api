from .base import *  # noqa 401
from .base import env

DEBUG = True

SECRET_KEY = env("SIGNING_KEY")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "ifssouy001@gmail.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Restaurant API"
