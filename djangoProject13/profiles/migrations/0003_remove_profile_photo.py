# Generated by Django 5.0.1 on 2024-01-14 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_photo_profile_telegram_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
    ]