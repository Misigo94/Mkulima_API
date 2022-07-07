from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = None
    name = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    is_farmer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Feeds(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='media/posts', default="default.jpg")
    description = models.TextField(max_length=300, blank=True)
    comments = models.ManyToManyField(
        'Comment', related_name='farmer_post', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    feeds = models.ForeignKey(Feeds, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Merchandise(models.Model):
    name = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='media/merchandise', default="default.jpg")
    date_posted = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


