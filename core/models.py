from django.db import models
from django.db.models.query import QuerySet

# Create your models here.
class Series(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

class Volume(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class Message(models.Model):

    class MessageObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published', 'Published'),
    )

    series = models.ForeignKey(Series, related_name='message', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    synopsis = models.TextField(null=True)
    file = models.FileField(upload_to='uploads/message/', blank=True)
    flyer = models.ImageField(upload_to='uploads/message_flyer/', blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='date')
    date = models.DateField()
    status = models.CharField(max_length=50, choices=options, default='draft')
    uploader = models.CharField(max_length=50)

    objects = models.Manager()
    message_objects = MessageObjects()
        

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title
    

class Announcement(models.Model):

    class AnnouncementObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    description = models.TextField()
    flyer = models.ImageField(upload_to='uploads/announcement_flyer/', blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    calendar_link = models.URLField()
    slug = models.SlugField(max_length=250, unique_for_date='start_date')
    status = models.CharField(max_length=50, choices=options, default='draft')

    objects = models.Manager()
    announcement_objects = AnnouncementObjects()

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return self.title
    

class Song(models.Model):

    class SongObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published', 'Published'),
    )

    volume = models.ForeignKey(Volume, related_name='song', on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='uploads/song/', blank=True)
    lyrics = models.FileField(upload_to='uploads/song_lyrics/', blank=True)
    cover = models.ImageField(upload_to='uploads/song_cover/', blank=True)
    slug = models.SlugField(max_length=250)
    status = models.CharField(max_length=50, choices=options, default='draft')

    objects = models.Manager()
    song_objects = SongObjects()

    def __str__(self):
        return self.title


class Testimony(models.Model):

    class TestimonyObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    content = models.TextField()
    status = models.CharField(max_length=50, choices=options, default='draft')

    objects = models.Manager()
    testimony_objects = TestimonyObjects()

    def __str__(self):
        return self.title
