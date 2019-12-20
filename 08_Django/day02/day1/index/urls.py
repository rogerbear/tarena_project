from django.conf.urls import url
from .views import *

urlpatterns = [
    # 如果访问路径(http://localhost:8000)后什么都没有的话
    url(r'^$', index_views),
    url(r'^login/$', login_views),
    url(r'^register/$', register_views),
    # 访问路径　http://localhost:8000/show
    url(r'^show/$', show_views, name='ss'),
    # 访问路径　http://localhost:8000/name
    url(r'^name/$', name_views),
    # 访问路径　http://localhost:8000/params/４位数字
    url(r'^params/(\d{4})/$', params_views, name='pa'),
    # http://localhost:8000/var
    url(r'^var/$', var_views),
    url(r'^baoqiang/$', baoqiang_views),
]
