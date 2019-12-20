from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def request_views(request):
    # print(dir(request))
    scheme = request.scheme
    body = request.body
    path = request.path
    method = request.method
    host = request.get_host()
    get = request.GET
    post = request.POST
    cookies = request.COOKIES

    return render(request, '01_request.html', locals())


def get_views(request):
    return render(request, '02_get.html')


def getdo_views(request):
    # print(request.GET)
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    return HttpResponse('用户名:' + uname + '密码:' + upwd)


def form_views(request):
    # 根据请求的意图决定该干什么
    # 如果是　get　请求的话，则显示03_form.html
    if request.method == 'GET':
        return render(request, '03_form.html')
    else:
        # 如果是　post　请求的话，则处理提交的数据
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        return HttpResponse('用户名:' + uname + ',密码:' + upwd)
