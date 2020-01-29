from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:art_pk>/delete/', views.delt),
    path('<int:art_pk>/edit/', views.edit),
    path('<int:art_pk>/update/', views.update)
]

