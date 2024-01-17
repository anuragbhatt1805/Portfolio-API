from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid, os

class UserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        """Create and save a new user"""
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, **extra_fields):
        """Create and save a new superuser"""
        user = self.create_user(password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()


def adminPic(instance, filepath):
    "Function for Profile Picture"
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('image', 'picture', filename)

class AdminDomain(models.Model):
    domain = models.CharField(max_length=255)
    objects = models.Manager()

class AreaOfInterest(models.Model):
    area = models.CharField(max_length=255)
    objects = models.Manager()


class AdminData(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # Contact Details
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)

    # Address Details
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    # About
    about = models.TextField()

    # Domains
    domains = models.ManyToManyField(AdminDomain)
    interests = models.ManyToManyField(AreaOfInterest)

    # Tagline
    tagline = models.CharField(max_length=255)

    # Social Media Links
    instagram = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)
    github = models.URLField(max_length=255)

    # Picture
    picture = models.ImageField(upload_to=adminPic, null=True)
