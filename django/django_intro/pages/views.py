from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):    # 첫 인자는 반드시 request(요청을 받아야 실행)
    return render(request, 'pages/index.html')


def introduce(request):
    return render(request, 'pages/introduce.html')


# template vraible example
def dinner(request, name):
    menu = ['Chicken', 'Pork', 'Beef']
    target = random.choice(menu)
    context = {
        'pick': target,
        'name': name
    }
    return render(request, 'pages/dinner.html', context)


def img(request):
    image = 'https://picsum.photos/500/700.jpg'
    context = {
        'image': image,
    }
    return render(request, 'pages/img.html',  context)


# ! ** variable routing ** !
def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'pages/greeting.html', context)


def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'res': result,
    }
    return render(request, 'pages/times.html', context)
    

def template_language(request):
    menus = ['aa', 'bb', 'cc', 'dd']
    my_sentence = 'life is short , you need python'
    messages = ['mango', 'apple', 'huha', 'power', 'caotic']
    now = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'now': now,
        'empty_list': empty_list
    }
    return render(request, 'pages/template_language.html', context)


def search(request):

    return render(request, 'pages/search.html')


def result(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    context = {
        'query':query,
        'category':category,
    }
    return render(request, 'pages/result.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')