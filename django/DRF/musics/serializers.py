from rest_framework import serializers
from .models import *

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id', )


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ['id', 'name']


class ArtistDetailSerializer(serializers.ModelSerializer): # ArtistSerializer 가능
    musics = MusicSerializer(many=True)
    musics_count = serializers.IntegerField(source='musics.count') # 필드추가; 카운트하는 방법임 (like all())

    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ['musics', 'musics_count']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'music_id', 'content',)