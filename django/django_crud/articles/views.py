from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.

## REST API

### uri를 정의하는 것은 method(GET, POST, DELETE, UPDATE)로만!!

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


# (index)GET >> page만 받아감
# (create)POST >> 정보를 작성
#   -->> create로 합칠 수 있음 

# def new(request):
#     return render(request, 'articles/new.html')


def create(request):
    '''
    만약 GET요청이면 html rendering
    POST라면 사용자데이터 받아서 article 생성
    '''
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()
        
        context = {
            'title': title,
            'content': content,
        }

        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/create.html')


def detail(request, id):
    # 이제 get_object_or_404
    # article = Article.objects.get(pk=id)
    article = get_object_or_404(Article, pk=id)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def delete(request, id):
    
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')

    else:
        # POST가 아닐경우 처리방법 가지고 있어야 함
        return redirect('articles:detail', id)


def update(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', id)
    else:
        # title = Article.GET.get('title')
        # content = Article.GET.get('content')

        context = {
            # 'title': title,
            # 'content': content,
            'article': article
        }
        return render(request, 'articles/update.html', context)