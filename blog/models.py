from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)