from django.shortcuts import render
from django.http import HttpResponse
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
