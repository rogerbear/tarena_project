from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_views(request):
    return HttpResponse('这是news应用中的index视图')


def params_views(request):
    return render(request, '01_params.html')


def cal_views(request, num1, num2):
    result = int(num1) + int(num2)
    return HttpResponse(result)
