# Generated by Django 5.0.6 on 2024-07-03 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_bookmark_like_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='like_count',
        ),
    ]