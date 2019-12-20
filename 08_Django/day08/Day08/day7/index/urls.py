from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_form/$', form1_views),
    url(r'^02_register/$', register_views),
    url(r'^03_login/$', login_views),
]

urlpatterns += [
    url(r'^04_widget1', widget1_views),
    url(r'^05_widget2', widget2_views),
]

urlpatterns += [
    url(r'^06_cookie1/$', cookie1_views),
    url(r'^07_cookie2/$', cookie2_views),
    url(r'^08_cookie3/$', cookie3_views),
    url(r'^09_getCookie/$', getCookie_views),
]

urlpatterns += [
    url(r'^10_setSession/$', setSession_views),
    url(r'^11_getSession/$', getSession_views),
    url(r'^12_delSession/$', delSession_views),
]
