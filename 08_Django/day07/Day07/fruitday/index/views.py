from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.


def login_views(request):
    # 根据用户的请求意图决定该干什么事情
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 处理用户登录操作
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        users = Users.objects.filter(uphone=uphone, upwd=upwd)
        if users:
            return HttpResponseRedirect('/')
        else:
            errMsg = '用户名或密码不正确'
            return render(request, 'login.html', locals())


def index_views(request):
    return render(request, 'index.html')


def register_views(request):
    # return render(request, 'register.html')
    # 根据用户的请求意图决定到底该做什么操作
    # 如　：get　请求，查看注册页面
    # 如　：post　请求，处理提交数据(注册)

    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uphone = request.POST['uphone']
        # 判断uphone在数据库中是否存在
        users = Users.objects.filter(uphone=uphone)
        if users:
            # 说明用户已经存在
            errMsg = '电话号码已存在，请重新输入'
            return render(request, 'register.html', locals())
        upwd = request.POST['upwd']
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        Users.objects.create(uphone=uphone, upwd=upwd,
                             uname=uname, uemail=uemail)
        return HttpResponseRedirect('/login/')
