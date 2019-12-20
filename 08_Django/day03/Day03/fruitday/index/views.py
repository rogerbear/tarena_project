from django.shortcuts import render

# Create your views here.


def login_views(request):
    return render(request, 'login.html')


def index_views(request):
    return render(request, 'index.html')


def register_views(request):
    return render(request, 'register.html')
