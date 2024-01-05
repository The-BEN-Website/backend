from django.urls import path
from .views import MessageList, MessageDetail, AnnouncementList, AnnouncementDetail, SongList, SongDetail, TestimonyList, TestimonyDetail

app_name = 'api'

urlpatterns = [
    path('message/<int:pk>/', MessageDetail.as_view(), name='message_detail'),
    path('message', MessageList.as_view(), name='message_list'),
    path('announce/<int:pk>/', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('announce', AnnouncementList.as_view(), name='announcement_list'),
    path('song/<int:pk>/', SongDetail.as_view(), name='song_detail'),
    path('song', SongList.as_view(), name='song_list'),
    path('testimony/<int:pk>/', TestimonyDetail.as_view(), name='testimony_detail'),
    path('testimony', TestimonyList.as_view(), name='testimony_list'),
]
