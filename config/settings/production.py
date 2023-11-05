from .base import *

# Over writing settings from base with production settings

SECRET_KEY = env('SECRET_KEY')

PORT = env('PORT')

DEBUG = env('DEBUG', default=False)

CSRF_TRUSTED_ORIGINS = ["https://pushnote-api-production.up.railway.app"]

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(' ')
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', " ").split(' ')
CORS_ORIGIN_ALLOW_ALL = os.getenv('CORS_ORIGIN_ALLOW_ALL', "False")
CORS_ORIGIN_ALLOW_ALL = CORS_ORIGIN_ALLOW_ALL == "True"
