from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Blog, BlogLike


@receiver(post_save, sender=BlogLike)
def update_blog(sender, instance, created, **kwargs):

    if created:
        print(sender)
        print(instance)
        Blog.objects.filter(
            id=instance.blog.id
        ).update(total_likes=instance.blog.total_likes + 1)


# post_save.connect(update_blog, sender=BlogLike)
