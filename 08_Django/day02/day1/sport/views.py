from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_views(request):
    ret = "这是sport应用中的index_views视图"
    return HttpResponse(ret)
