from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() # 필수 매개변수 x
    created_at = models.DateTimeField(auto_now_add=True)

