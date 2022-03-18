from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from strgen import StringGenerator as SG
from .models import Story, Reply, StoryLike, ReplyComment
from .utils import clean_html


@receiver(pre_save, sender=Story)
def create_code(sender, instance, **kwargs):
    if instance._state.adding:
        instance.code = SG(r"[\w]{10}").render()


@receiver(pre_save, sender=Story)
def update_content_safe(sender, instance, **kwargs):
    # Dùng cho pre_save
    instance.content_safe = clean_html(instance.content)

@receiver(pre_save, sender=Reply)
def update_content_safe(sender, instance, **kwargs):
    # Dùng cho pre_save
    instance.content_safe = clean_html(instance.content)


@receiver(post_save, sender=StoryLike)
def update_blog(sender, instance, created, **kwargs):
    # Dùng cho post_save
    if created:
        Story.objects.filter(
            id=instance.story.id
        ).update(num_likes=instance.story.num_likes + 1)


@receiver(post_save, sender=Reply)
def update_blog(sender, instance, created, **kwargs):
    # Dùng cho post_save
    if created:
        Reply.objects.filter(
            id=instance.story.id
        ).update(num_likes=instance.story.num_comments + 1)


@receiver(post_save, sender=ReplyComment)
def update_blog(sender, instance, created, **kwargs):
    # Dùng cho post_save
    if created:
        ReplyComment.objects.filter(
            id=instance.story.id
        ).update(num_likes=instance.story.num_replies + 1)
