from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# class CustomAccountManager(BaseUserManager):
#     def create_superuser(self, email, user_name, first_name, password, **other_fields):
#         other_fields.setdefault('is_staff',True)
#         other_fields.setdefault('is_superuser',True)
#         other_fields.setdefault('is_active',True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must be assigned to is_staff = True')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must be assigned to is_superuser = True')
        
#         return self.create(self, email, user_name, first_name, password, **other_fields)
    
#     def create_user(self, email, user_name, first_name, password, **other_fields):
#         if not email:
#             raise ValueError(_('you must provide email address'))
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff = True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser = True')
        
        # Use create_user method to create the superuser
        return self.create_user(email, user_name, first_name, password, **other_fields)
    
    # The create_user method remains unchanged
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user



class NewUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ICT = "ICT", 'ICT'
        MEDIA = "MEDIA", 'MEDIA'
        PUBLICATION = "PUBLICATION", 'PUBLICATION'
        MUSIC = "MUSIC", 'MUSIC'
        NIL = "NIL", 'NIL'

    base_role = Role.ICT

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=50, choices=Role.choices)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        
    def __str__(self):
        return self.user_name

class MediaManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=NewUser.Role.MEDIA)
    
class Media(NewUser):
    base_role = NewUser.Role.MEDIA

    media = MediaManager()

    class Meta:
        proxy = True 

class PublicationManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=NewUser.Role.PUBLICATION)
    
class Publication(NewUser):
    base_role = NewUser.Role.PUBLICATION

    media = PublicationManager()

    class Meta:
        proxy = True 

class IctManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=NewUser.Role.ICT)
    
class Ict(NewUser):
    base_role = NewUser.Role.ICT

    ict = PublicationManager()

    class Meta:
        proxy = True 

class MusicManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=NewUser.Role.MUSIC)
    
class Music(NewUser):
    base_role = NewUser.Role.MUSIC

    ict = MusicManager()

    class Meta:
        proxy = True 
