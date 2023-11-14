# Generated by Django 4.2.7 on 2023-11-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('telegram', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('major', models.CharField(blank=True, max_length=255, null=True)),
                ('course', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('favorite_book', models.CharField(max_length=255)),
                ('favorite_movie', models.CharField(max_length=255)),
                ('favorite_quote', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]