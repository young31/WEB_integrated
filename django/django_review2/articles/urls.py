from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # article
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name="detail"),
    path('edit/<int:article_pk>/', views.update, name="update"),
    path('delete/<int:article_pk>/', views.delete, name="delete"),
    # comment
    path('create_comment/<article_pk>', views.create_comment, name="create_comment"),
    path('delete_comment/<article_pk>/<comment_pk>', views.delete_comment, name="delete_comment"),
    # user relationship
    path('like/<article_pk>/', views.like, name='like'),
    path('<article_pk>/follow/<user_pk>', views.follow, name='follow'),
]
