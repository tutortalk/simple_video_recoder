from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^$', 'recorder.views.home', name='home'),
    url(r'^start/(?P<rtmp_stream>[0-9]+)/$', 'recorder.views.start', name='start'),
    url(r'^stop/(?P<rtmp_stream>[0-9]+)/$', 'recorder.views.stop', name='stop'),
    url(r'^live/', 'recorder.views.live', name='live'),
    url(r'^delete-video/$', 'recorder.views.delete_video', name='delete-video'),
    url(
        r'^config\.xml',
        TemplateView.as_view(template_name='recorder_config.xml',
            content_type='text/xml',
            get_context_data=lambda: {'rtmp_server': settings.RTMP_SERVER},
        )
    ),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
