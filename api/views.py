from rest_framework import generics
from core.models import Message, Announcement, Song, Testimony
from .serializers import MessageSerializer, AnnouncementSerializer, SongSerializer, TestimonySerializer

# Create your views here.
class MessageList(generics.ListAPIView):
    queryset = Message.message_objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class AnnouncementList(generics.ListAPIView):
    queryset = Announcement.announcement_objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementDetail(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class SongList(generics.ListAPIView):
    queryset = Song.song_objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class TestimonyList(generics.ListAPIView):
    queryset = Testimony.testimony_objects.all()
    serializer_class = TestimonySerializer

class TestimonyDetail(generics.RetrieveAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
