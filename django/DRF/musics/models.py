from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    
    def __str__(self):
        return f'{self.music.pk} - {self.pk}댓글'

    