from django.urls import path, include
from . import views

# xxx/pages/___
urlpatterns = [
    path('', views.index), # 이미 다 만들어진 url주소를 받기 때문에 추가 입력 불필요
    path('greeting/<str:name>', views.greeting)
]
