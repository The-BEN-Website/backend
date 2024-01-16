from rest_framework import generics
from core.models import Message, Announcement, Song, Testimony, Gallery
from .serializers import MessageSerializer, AnnouncementSerializer, SongSerializer, TestimonySerializer, GallerySerializer
from .permision import PublicationTeam, MusicTeam, MediaTeam, Pub

# Create your views here.
class MessageList(generics.ListAPIView):
    """
    This view displays all the messages that have been marked as published
    """
    queryset = Message.message_objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageCreateview(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [Pub]

class MessageManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [Pub]


class AnnouncementList(generics.ListAPIView):
    queryset = Announcement.announcement_objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementDetail(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementCreateview(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [PublicationTeam]

class AnnouncementManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [PublicationTeam]


class SongList(generics.ListAPIView):
    queryset = Song.song_objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongCreateview(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [MusicTeam]

class SongManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [MusicTeam]


class TestimonyList(generics.ListAPIView):
    queryset = Testimony.testimony_objects.all()
    serializer_class = TestimonySerializer

class TestimonyDetail(generics.RetrieveAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer

class TestimonyCreateview(generics.CreateAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
    permission_classes = [PublicationTeam]

class TestimonyManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
    permission_classes = [PublicationTeam]


class GalleryList(generics.ListAPIView):
    queryset = Gallery.gallery_objects.all()
    serializer_class = GallerySerializer

class GalleryDetail(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class GalleryCreateview(generics.CreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [MediaTeam]

class GalleryManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [MediaTeam]
