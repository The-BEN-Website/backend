from rest_framework import serializers
from core.models import Message, Announcement, Song, Testimony, Gallery


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id','series','title','synopsis','date',)


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id','title','description','start_date','end_date','calendar_link',)


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id','volume','title',)


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ('id','title','author','content',)

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id','title',)

