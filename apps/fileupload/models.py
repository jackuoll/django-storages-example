from django.db import models
from custom_storage import TotallyOtherPrivateStorage

class FileUpload(models.Model):
    file = models.FileField()

class FileUploadInAnotherBucket(models.Model):
    file_in_other_bucket = models.FileField(storage=TotallyOtherPrivateStorage())
