from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from strgen import StringGenerator as SG
from .models import Story
from .utils import clean_html


@receiver(pre_save, sender=Story)
def create_code(sender, instance, **kwargs):
    if instance._state.adding:
        instance.code = SG(r"[\w]{10}").render()


@receiver(pre_save, sender=Story)
def update_content_safe(sender, instance, **kwargs):
    # Dùng cho pre_save
    instance.content_safe = clean_html(instance.content)

