from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True)
    slug = AutoSlugField(unique=True, editable=True, blank=True)
    desc_safe = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    color_code = models.CharField(max_length=10, default="#0a8ddf")


class Story(models.Model):
    code = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, related_name='+', on_delete=models.PROTECT)
    content = models.TextField(blank=True)
    content_safe = models.TextField(blank=True)
    title = models.CharField(max_length=255, blank=True)
    category = models.ManyToManyField(Category, related_name='+', blank=True)
    last_activity_by = models.ForeignKey(User, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
    last_activity_at = models.DateTimeField(auto_now_add=True, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True, editable=True)
    STORY_STATUS_CHOICES = (
        ('P', 'Công Khai'),
        ('R', 'Đã Xóa'),
        ('S', 'Đang Lên Lịch'),
    )
    status = models.CharField(default='P', db_index=True, max_length=1, choices=STORY_STATUS_CHOICES)
    closed = models.BooleanField(default=False, db_index=True)
    featured_until = models.DateTimeField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    edited_at = models.DateTimeField(blank=True, null=True)
    edited_by = models.ForeignKey(User, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
    num_views = models.PositiveIntegerField(default=0)
    num_likes = models.PositiveIntegerField(default=0)
    num_replies = models.PositiveIntegerField(default=0)
    num_comments = models.PositiveIntegerField(default=0)
    num_participants = models.PositiveIntegerField(default=-1)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)


class Reply(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.PROTECT)
    story = models.ForeignKey(Story, related_name='replies', on_delete=models.CASCADE)
    reply_order = models.IntegerField(default=0)
    content = models.TextField(blank=True)
    content_safe = models.TextField(blank=True)
    removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)
    edited_at = models.DateTimeField(blank=True, null=True)
    edited_by = models.ForeignKey(User, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
