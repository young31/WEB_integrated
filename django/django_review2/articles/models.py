from django.db import models
from django.core.validators import EmailValidator, MinValueValidator
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, # settings 가보면 새로 정의한거 들어가있음
        on_delete=models.CASCADE,
        related_name='articles') # related_name없으면 _set으로 자동 설정
    # user에서 쓸때만 setting에서 직접갖고옴!!
    ## 장고 실행순서와 연관있는부분으로 이 부분만 그런다는 것을 주목
    
    liked_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='liked_articles'
    )
    class Meta:
        ordering = ('-pk', )


class Person(models.Model):
    name=models.CharField(max_length=10)
    email=models.CharField(
        max_length=100,
        validators=[EmailValidator(message='email format xx')]    
    )
    age=models.IntegerField(
        validators=[MinValueValidator(19, message='under 19 xx')]
    )

class Comment(models.Model):
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-pk']

