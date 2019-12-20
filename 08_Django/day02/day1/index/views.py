from django.shortcuts import render
from django.http import HttpResponse
# 通过loader.get_template()加载模板
from django.template import loader

# Create your views here.


# def index_views(request):
#     # 1.通过loader加载01_index.html模板，并保存给t
#     t = loader.get_template('01_index.html')
#     # ２．通过t将模板渲染成字符串(允许传递变量)
#     dic = {
#         'title': '哆啦Ａ梦',
#         'author': '藤子Ｆ不二雄',
#     }
#     html = t.render(dic)  # 传递变量到模板中
#     # html = t.render()  #不传递变量
#     # ３．通过HttpResponse将字符串响应给浏览器
#     return HttpResponse(html)


def index_views(request):
    dic = {
        'title': '火影忍者',
        'author': '岸xxxx'
    }
    return render(request, '01_index.html', dic)


def login_views(request):
    return HttpResponse('这是登录页面')


def register_views(request):
    return HttpResponse('这是注册页面')


def show_views(request):
    dic = {
        'name': '绿光',
        'author': '王宝强',
        'music': '贾乃亮',
        'singer': '陈羽凡',
    }
    return render(request, '02_show.html', dic)


def name_views(request):
    return render(request, '03_name.html')


def params_views(request, num):
    return HttpResponse('参数是:' + num)


def var_views(request):
    lis = ['张三丰', '张翠山', '张无忌']
    tup = ('金花婆婆', '殷素素', '赵敏')
    dic = {
        "a": "Android",
        "b": "Beyond",
        "c": "CUP",
    }

    param = {
        'list': lis,
        'tup': tup,
        'dic': dic,
        'str': 'Hello Django',
        'num': 1314,
        'fun': fun(),
        'A': A(),
    }
    return render(request, '04_var.html', param)


def fun():
    return 'fun函数'


class A(object):
    def f(self):
        return 'Class A　中的　f函数'


def baoqiang_views(request):
    return render(request, '05_static.html')
