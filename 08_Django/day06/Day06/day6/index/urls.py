from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_request/$', request_views),
    url(r'^02_get/$', get_views),
    url(r'^03_getdo/$', getdo_views),
    url(r'^04_form/$', form_views),
]
