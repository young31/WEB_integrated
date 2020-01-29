from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),
    path('search/', views.search),
    path('result/', views.result),
    path('dinner/<str:name>/', views.dinner),
    path('index/', views.index), 
    path('img/', views.img),
    path('greeting/<str:name>/', views.greeting),
    path('times/<int:num1>_<int:num2>/', views.times),
    path('introduce/', views.introduce),
    path('template_language/', views.template_language),
]