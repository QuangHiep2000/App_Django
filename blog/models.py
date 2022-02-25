from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)


class Blog(models.Model):
    category = models.ForeignKey(Category, related_name='+', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse("url_api_content_blog", kwargs={"slug": self.slug})


