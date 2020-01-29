from django.urls import path
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Music API',
        default_version='v1',
        description='음악관련 서비스',
    )
)

app_name = 'musics'
urlpatterns = [
    # db
    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:music_pk>/', views.music_detail_update_delete, name='music_detail_update_delete'),
    path('musics/<int:music_pk>/comments/', views.comments_create, name='comments_create'),

    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:artist_pk>/', views.artist_detail_update_delete, name='artist+detail'),

    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:comment_pk>/', views.comment_update_delete, name='comment_update_delete'),

    # doc
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
]
