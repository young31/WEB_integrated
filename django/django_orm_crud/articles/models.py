from django.db import models

# Create your models here.

class Article(models.Model):
    # id = models.AutoField(primary_key=True)
    # id(pk)는 처음 테이블이 생성될 때 자동으로 만들어짐  >>  따로 작성안해도 됨
    # 모든 필드는 기본적으로 NOT NULL > 비어있으면 안됨!

    title = models.CharField(max_length=20) # db필드(col), max_length가 필수 인자
    content = models.TextField() # db필드
    created_at = models.DateTimeField(auto_now_add=True) # add와 아닌 것의 차이
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}th - {self.title} : {self.content}'
    