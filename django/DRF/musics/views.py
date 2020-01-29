from django.shortcuts import render, get_object_or_404
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer

# from django_extensions import Ipy
# Create your views here.

@api_view(['GET'])
def music_list(request):
    # query 구현(artist_id가 넘어온다면)
    params = {}
    artist_id = request.GET.get('artist_id') # 쿼리문은 get으로 넘어옴
    if artist_id is not None:
        params['artist_id'] = artist_id

    musics= Music.objects.filter(**params) # 빈값이면 전체반환이므로 조건문 단축가능

    serializer = MusicSerializer(musics, many=True)

    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def music_detail_update_delete(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method=='GET':
        serializer = MusicSerializer(data=request.data, instance=music)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(data=request.data, instance=music)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'meassage': "create successfully"})
    else:
        music.delete()
        return Response({'message': 'successfully deleted'})



@api_view(['POST']) #post!!
def comments_create(request, music_pk):
    # comment는 텍스트로 올것 > deserialize필요!
    ## serializer가 일해줌
    serializer = CommentSerializer(data=request.data) # modelform처럼 체크해줌
    if serializer.is_valid(raise_exception=True): # raise_exception: 검증실패하면 400 error
        serializer.save(music_id=music_pk)
    return Response(serializer.data)

######## rasie_exception 처리
# if serializer.is_valid(raise_exception=True): 
#     serializer.save(music_id=music_pk)
# else:
#     return --
# #######

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)

    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail_update_delete(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method=='GET':
        serializer = ArtistDetailSerializer(artist)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = ArtistSerializer(data=request.data, instance=artist)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'successfully updated'})
    else:  
        artist.delete()
        return Response({'message': 'successfully deleted'})


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':"comment has been updated"}) # serializer.data
    else: # DELETE
        comment.delete()
        return Response({'message': "comment has been deleted"})