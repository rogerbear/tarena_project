from django.conf.urls import url
from .views import *

urlpatterns = [
    # 访问路径是　index 的时候，交给index_views去处理
    # http://localhost:8000/news/index/
    url(r'^index/$', index_views),
]
