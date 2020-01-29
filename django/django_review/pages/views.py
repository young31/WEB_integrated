from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def greeting(request, name):
    return render(request, 'pages/greeting.html')
