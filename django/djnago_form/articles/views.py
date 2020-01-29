from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)


# GET: 생성페이지
# POST: 생성로직
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')

        ### 밑처럼 바로 받는 것 보다 거쳐서 받는 것이 좋다
        # title = request.POST.get('title')
        # content = request.POST.get('content')
            article = Article(title=title, content=content) 
            article.save()
            return redirect('articles:index')
        # 코드 구조
        # else:
        #     context = {'form':form}
        #     return render(request, 'articles/create.html', context)

    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)
