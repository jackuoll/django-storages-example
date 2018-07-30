from django.contrib.admin.views.decorators import staff_member_required
from django.views import View
from django.http import HttpResponseForbidden, HttpResponse
from tempfile import NamedTemporaryFile
from custom_storage import MyPrivateStaticStorage


class S3DownloadView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_staff:
            return HttpResponseForbidden("Not permitted")
        # todo: different types of storages, validate this file should get gettable by this user
        to_get = kwargs['download_s3_url']
        mss = MyPrivateStaticStorage()
        with NamedTemporaryFile() as tf:
            mss.bucket.download_fileobj(f'{mss.location}/{to_get}', tf)
            tf.seek(0)
            response = HttpResponse(tf.read(), content_type='application/force-download')
            response['Content-Disposition']=f'attachment; filename="{to_get}"'
            return response
