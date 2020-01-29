from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)  # 빈값도 저장 가능 >> 데이터 유효성과 관련
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'queality': 90},
    )
    ## blank vs null >> null -> db와 관련(null이라는 값을 저장 하냐)
    ## ** convention >> text관련은 ''로(숫자는 가능), 이미지는 null로 **
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    # on_delete=models.CASCADE == 'Article 이 삭제되면 Comment 도 함께 삭제'
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    # comment_set은 default로 사용되고 이를 comments로 받아야지
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 역순으로 가져올 수 있도록 
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content



