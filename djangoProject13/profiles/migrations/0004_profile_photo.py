# Generated by Django 5.0.1 on 2024-01-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profiles/%Y/%m/%d/'),
        ),
    ]