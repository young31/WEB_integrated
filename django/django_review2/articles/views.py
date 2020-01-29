from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from IPython import embed
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse, JsonResponse
# Create your views here.
# @login_required(login_url='/accounts/login/')

@login_required
def create(request):
    if request.method == 'POST': # Aticle create
        form = ArticleForm(request.POST)
        if form.is_valid(): # form은 정의된 field만 검사함
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)

    else: # show page to write
        form = ArticleForm()
    
    # 위 if ~ else결과와 아래 else결과가 중복되므로 아예 빼서 실행되게 함
    context = {'form': form}
    return render(request, 'articles/create.html', context)


@require_GET
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    forms = CommentForm()
    comments = article.comments.all()
    context = {
        'article':article,
        'form':forms,
        'comments': comments,
    }

    return render(request, 'articles/detail.html', context)


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if article.user == request.user: # 작성자만 수정가능하게
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article_pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail', article_pk)
    context = {'form':form}
    return render(request, 'articles/update.html', context)


# redirect는 get요청만 가능하므로 post요청 작업은 login_requiered사용 불가
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.user == request.user:
            article.delete()
            return redirect('articles:index')
        else:
            return redirect('articles:detail', article_pk)
    else:
        return redirect('articles:detail', article_pk)


# comment
@require_POST
def create_comment(request, article_pk):
    if request.user.is_authenticated:
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_id = article_pk
            comment.user = request.user
            comment.save()
    return redirect('articles:detail', article_pk)


@require_POST
def delete_comment(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment=get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            article=get_object_or_404(Article, pk=article_pk)
            comment.delete()
            return redirect('articles:detail', article_pk)
        else:
            return redirect('articles:detail', article_pk)
    else:
        return HttpResponse('login plz', status=401)


def like(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    
    if article.liked_users.filter(pk=user.pk).exists():
        user.liked_articles.remove(article)
        liked = False
    else:
        user.liked_articles.add(article)
        liked = True
    # user.save()

    context = {
        'liked': liked,
        'count': article.liked_users.count()
        }
    return JsonResponse(context)


@login_required
def follow(request, article_pk, user_pk):
    user = request.user # login uesr
    person = get_object_or_404(get_user_model(), pk=user_pk) # article master
    
    if user in person.followers.all(): # already follow > unfol
        person.followers.remove(user)
    else:
        person.followers.add(user)
    return redirect('articles:detail', article_pk)