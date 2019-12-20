from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_form/$', form1_views),
    url(r'^02_register/$', register_views),
    url(r'^03_login/$', login_views),
]
