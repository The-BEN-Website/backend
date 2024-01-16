from django.urls import path
from .views import MessageList, MessageDetail, MessageCreateview, MessageManageView, AnnouncementList, AnnouncementDetail, AnnouncementCreateview, AnnouncementManageView, SongList, SongDetail, SongCreateview, SongManageView, TestimonyList, TestimonyDetail, TestimonyCreateview, TestimonyManageView, GalleryList, GalleryDetail, GalleryCreateview, GalleryManageView

app_name = 'api'

urlpatterns = [
    path('message/<int:pk>/', MessageDetail.as_view(), name='message_detail'),
    path('message', MessageList.as_view(), name='message_list'),
    path('message_create', MessageCreateview.as_view(), name='message_create'),
    path('message_manage/<int:pk>/', MessageManageView.as_view(), name='message_manage'),

    path('announce/<int:pk>/', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('announce', AnnouncementList.as_view(), name='announcement_list'),
    path('announce_create', AnnouncementCreateview.as_view(), name='announce_create'),
    path('announce_manage/<int:pk>/', AnnouncementManageView.as_view(), name='announce_manage'),

    path('song/<int:pk>/', SongDetail.as_view(), name='song_detail'),
    path('song', SongList.as_view(), name='song_list'),
    path('song_create', SongCreateview.as_view(), name='song_create'),
    path('song_manage/<int:pk>/', SongManageView.as_view(), name='song_manage'),

    path('testimony/<int:pk>/', TestimonyDetail.as_view(), name='testimony_detail'),
    path('testimony', TestimonyList.as_view(), name='testimony_list'),
    path('testimony_create', TestimonyCreateview.as_view(), name='testimony_create'),
    path('testimony_manage/<int:pk>/', TestimonyManageView.as_view(), name='testimony_manage'),

    path('gallery/<int:pk>/', GalleryDetail.as_view(), name='gallery_detail'),
    path('gallery', GalleryList.as_view(), name='gallery'),
    path('gallery_create', GalleryCreateview.as_view(), name='gallery_create'),
    path('gallery_manage/<int:pk>/', GalleryManageView.as_view(), name='gallery_manage'),
]
