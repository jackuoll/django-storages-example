# django-storages-example
Using django-storages for static and uploads

Guide taken from: https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/

apps.fileupload uses a folder within the s3 bucket called 'private-folder', as defined in custom_storage.py and referenced in settings.

While the django staticfiles use 'static' within the same bucket for storage, and are by default, public.

Open pull requests by myself are purely there for reference.
