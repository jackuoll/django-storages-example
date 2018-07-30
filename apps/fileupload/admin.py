from django.contrib import admin

from apps.fileupload.models import FileUpload


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('file', )


admin.site.register(FileUpload, FileUploadAdmin)
