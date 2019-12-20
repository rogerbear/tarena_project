from django.conf.urls import url
from .views import *

urlpatterns = [
    # 访问路径是　index 的时候，交给index_views去处理
    # http://localhost:8000/news/index/
    url(r'^$', index_views),

    # 访问路径是　localhost:8000/news/01_params 的时候
    url(r'^01_params/$', params_views),

    # localhost:8000/news/02_cal/35/72
    url(r'^02_cal/(\d+)/(\d+)/$', cal_views, name='cal'),
]
