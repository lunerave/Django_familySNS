# Generated by Django 5.0.6 on 2024-06-21 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='like_count',
            field=models.IntegerField(),
        ),
    ]
