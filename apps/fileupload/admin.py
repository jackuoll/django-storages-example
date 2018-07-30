from django.contrib import admin

from apps.fileupload.models import FileUpload

from django.utils.html import format_html


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('uploaded_file', )

    def uploaded_file(self, obj):
        # change the download link to be a proxy
        return format_html(f'<a href="/download_s3/{obj.file.name}">{obj.file.name}</a>')
    uploaded_file.allow_tags = True
    uploaded_file.short_description = 'Column description'


admin.site.register(FileUpload, FileUploadAdmin)
