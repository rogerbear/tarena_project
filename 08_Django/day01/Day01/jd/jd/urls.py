"""jd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# 将views.py模块中的run_views函数导入到当前模块中
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 编写自定义的url匹配模式　－　正则表达式
    url(r'^run/$', run_views),

    # 编写自定义的url匹配模式，fun/两位数字
    url(r'^fun/(\d{2})/$', fun_args1_views),

    # 编写自定义的url匹配模式，fun/四位数字/两位数字
    url(r'^fun/(\d{4})/(\d{2})/$', fun_args2_views),
]

urlpatterns += [
    url(r'^show/$', show_views, {'name': 'zsf', 'age': '25'}),
]
