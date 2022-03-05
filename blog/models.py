from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField



class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)


class Blog(models.Model):
    category = models.ForeignKey(Category, related_name='+', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    slug = AutoSlugField(max_length=255, unique=True, populate_from='title', editable=True, blank=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    total_likes = models.PositiveIntegerField(default=0)


class BlogLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # def get_absolute_url(self):
    #     return reverse("url_api_content_blog", kwargs={"slug": self.slug})

