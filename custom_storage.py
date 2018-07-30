from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MyPrivateStaticStorage(S3Boto3Storage):
    location = 'private-folder'
    default_acl = 'private'


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
