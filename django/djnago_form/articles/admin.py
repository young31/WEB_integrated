from django.contrib import admin
from .models import Article
# Register your models here.

@admin.register(Article)
class ArticelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
