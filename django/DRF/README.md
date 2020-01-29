# REST_DJANGO

## prereq
- django
- python
- pip install djangorestframework

## apply
- from rest_framework.decorators import api_view  
    >> @api_view(['GET'])  <<함수 위 decorators>>

- !! serialize: 다른 곳에서도 쓸 수 있게 변환하는 기술  
    >> json형식으로 만들어 줄 필요가 있음 !! 필수조건 (파이썬 -> 다른 언어등에서도 가능하게 해주는 역할) !!
    - 상황에 맞게 처리해줄 필요는 있음: 정보를 다 보여줄지 키 값만 보여줄지 등 서비스에 따라서

- serializers.py
    - define class(모델과 유사)
        - calss -> Meta

- view에서 func_serializer(target, ~many=True)로 wrap-up

- import Response >> return Response(serializer.data)

!! templates 만들 필요가 없다리 !!

## documentation
- pip install drf-yasg
- in urls.py
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Music API',
        default_version='v1',
        description='음악관련 서비스',
    )
)

- in urlpatterns
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger')

>> go to loaclhost:8888/docs or loaclhost:8888/swagger !! swagger 멋짐 폭발 !!

## RESTful 하게 명령어 조작
- uri/url은 리소스 정보만 표현 (localhost:pics/1/)
- 행위는 method로 구현
    - get, post, put, delete

## 쿼리요청 제어
- 쿼리는 GET.get()으로 잡을 수 있음
- 이후 dict형식으로 저장해서 (이 때 키값이 model이 갖고 있는 param값)
- content를 담을 조건에 추가해줌(.filter(---))