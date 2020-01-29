from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


# 장고 활용 유저 모델
## AbstractBaseUSer vs AbstractUser >> base가 더 정보가 적음(id, pw, 최종로그인)
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name="followees", # 지금같은경우는 반드시 있어야함(자기참조이므로로 추정)
        )
