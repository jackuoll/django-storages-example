from django.conf.urls import url

from . import views


class DownloadS3App(object):
    name = "download_s3"

    def get_urls(self):
        urlpatterns = [
            url(r'^(?P<download_s3_url>[a-zA-Z0-9-@._ ]+)/$', views.S3DownloadView.as_view(), name='download_s3'),
        ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), 'download_s3', self.name


download_s3 = DownloadS3App()
