from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


from django.contrib.auth.models import User
from .models import Blog, BlogLike
from .utils import clean_html


@receiver(post_save, sender=BlogLike)
def update_blog(sender, instance, created, **kwargs):
    print("nam")
    # Dùng cho post_save
    if created:
        Blog.objects.filter(
            id=instance.blog.id
        ).update(total_likes=instance.blog.total_likes + 1)
# post_save.connect(update_blog, sender=BlogLike)


@receiver(pre_save, sender=Blog)
def update_content_safe(sender, instance, **kwargs):
    print("hiep")
    # Dùng cho pre_save
    instance.content_safe = clean_html(instance.content)



