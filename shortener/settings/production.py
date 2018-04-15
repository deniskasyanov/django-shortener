from .base import *


ALLOWED_HOSTS = ['.herokuapp.com',]


MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
