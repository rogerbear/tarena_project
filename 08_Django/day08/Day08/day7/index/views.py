from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.


def form1_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request, '01_form.html', locals())
    else:
        # 获取提交的数据
        # subject = request.POST['subject']
        # email = request.POST['email']
        # message = request.POST['message']
        # topic = request.POST['topic']
        # isSave = request.POST['isSave']
        # return HttpResponse(subject + ',' + email + ',' + message + ',' +
        # topic + ',' + isSave)

        # 通过　forms.Form的构造函数接受post的数据
        form = RemarkForm(request.POST)
        # 判断是否通过所有验证
        if form.is_valid():
            # 必须通过验证后才能取值
            # 取值
            cd = form.cleaned_data
            print(cd['subject'])
            print(cd['email'])
            print(cd['message'])

        return HttpResponse("Get OK")


def register_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,
                      '02_register.html', locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            users = Users(**cd)
            users.save()
        return HttpResponse('Register OK')


def login_views(request):
    form = LoginForm()
    return render(request, '03_login.html', locals())


def widget1_views(request):
    form = WidgetForm2()
    return render(request, '04_widget.html', locals())


def widget2_views(request):
    form = WidgetForm3()
    return render(request, '04_widget.html', locals())


# 直接响应一句话给客户端
def cookie1_views(request):
    # 创建响应对象
    resp = HttpResponse('测试添加cookie')
    # 为响应对象设置要保存的cookie的值
    resp.set_cookie('uname1', 'zsf', 60 * 60)
    # 将响应对象响应给客户端
    return resp

# 使用模板添加cookie


def cookie2_views(request):
    # 创建一个响应对象
    resp = render(request, '05_cookie.html', locals())
    # 为响应对象设置要保存的cookie的值
    resp.set_cookie('uname2', 'wuji.zhang', 60 * 30)
    # 将响应对象响应给客户端
    return resp


def cookie3_views(request):
    # 创建响应对象 (重定向对象)
    resp = HttpResponseRedirect('/05_widget2/')
    # 设置cookie
    resp.set_cookie('uname3', 'zhaomin', 60 * 5)
    # 响应给客户端
    return resp


# 查看当前站点下的所有的cookie信息
def getCookie_views(request):
    # print(request.COOKIES)
    uname = request.COOKIES['uname1']
    return HttpResponse('uname1的值为:' + uname)


# 向session中存放数据
def setSession_views(request):
    request.session['uname'] = 'sanfeng.zhang'
    return HttpResponse('Add Session OK')


# 从 session中获取数据
def getSession_views(request):
    if 'uname' in request.session:
        uname = request.session.get('uname')
        return HttpResponse('session中的uname:' + uname)
    else:
        return HttpResponse('Sessioin中没有uname的值')


# 将 uname 从session中删除出去
def delSession_views(request):
    del request.session['uname']
    return HttpResponse('删除session成功,<a href="/11_getSession/">查看</a>')
