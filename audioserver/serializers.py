from rest_framework import serializers
from .models import Song
from .models import Podcast
from .models import Audiobook
from .models import Participant

class Song_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('songId','name', 'duration', 'upload_time')

class Participant_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('name')

class Podcast_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ('podId','name', 'duration', 'upload_time', 'host','participants')
        depth=1

class Audiobook_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = ('audioId','title', 'author', 'narrator', 'duration', 'upload_time')