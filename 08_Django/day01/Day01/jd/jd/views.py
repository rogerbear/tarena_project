from django.http import HttpResponse

# 编写视图处理函数，一个函数相当于是一个视图


def run_views(request):
    # 向客户端浏览器响应输出一句话
    return HttpResponse('我的第一个DJANGO程序')


# url(r'^fun/(\d{2})/$',fun_args1_views)
def fun_args1_views(request, num):
    return HttpResponse('参数是：' + num)


# localhost:8000/fun/2018/05
def fun_args2_views(request, num1, num2):
    return HttpResponse('参数１:' + num1 + ',参数２:' + num2)

# url(r'^show/$',show_views,{'name':'zsf','age':'25'}),


def show_views(request, name, age):
    return HttpResponse('name:' + name + ',age:' + age)
