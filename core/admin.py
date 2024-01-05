from django.contrib import admin
from core.models import Message, Announcement, Song, Testimony, Series, Volume

# Register your models here.
admin.site.register(Series)
admin.site.register(Message)
admin.site.register(Announcement)
admin.site.register(Volume)
admin.site.register(Song)
admin.site.register(Testimony)
