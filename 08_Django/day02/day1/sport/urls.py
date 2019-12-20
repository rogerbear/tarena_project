# sport应用中的路由文件　
# 主要匹配的是　sport/ 之后的访问路径(不包含sport/)

from django.conf.urls import url
from .views import *

urlpatterns = [
    # 如果请求路径是　index/ 交给index_views
    # http://localhost:8000/sport/index
    url(r'^$', index_views),
]
