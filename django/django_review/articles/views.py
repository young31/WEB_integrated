from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'arts': articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    art = Article()
    art.title = title
    art.content = content

    art.save()

    return redirect('/articles/')


def delt(request, art_pk):
    art = Article.objects.get(pk=art_pk)
    art.delete()
    return redirect('/articles/')
    # url주소를 지정할 때는 앞에 /필요
    # 파일 지정은 앞에 / 불필요 


def edit(request, art_pk):
    art = Article.objects.get(pk=art_pk)
    context = {'article': art}
    return render(request, 'articles/edit.html', context)


def update(request, art_pk):
    title = request.GET.get('title')
    content = request.GET.get('content')

    art = Article.objects.get(pk=art_pk)

    art.title = title
    art.content = content

    art.save()

    return redirect('/articles/')