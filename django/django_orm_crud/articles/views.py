from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# 사용자 입력 폼 제공
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # form에서 작성한 것을 추출 및 새롭게 저장
    # 완료되었다는 페이지 작성
    title = request.GET.get('title')
    content = request.GET.get('content')
    # querydict로 저장되어 들어옴
    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/create.html')