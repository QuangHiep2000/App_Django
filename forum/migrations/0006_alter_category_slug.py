# Generated by Django 3.2 on 2022-03-14 11:16

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_story_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='name', unique=True),
        ),
    ]
