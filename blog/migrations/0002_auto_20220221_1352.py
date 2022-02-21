# Generated by Django 3.2 on 2022-02-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manage',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='manage',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manage',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manage',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='manage',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
