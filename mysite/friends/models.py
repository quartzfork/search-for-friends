from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    telegram = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    major = models.CharField(max_length=255, blank=True, null=True)
    course = models.IntegerField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    favorite_book = models.CharField(max_length=255)
    favorite_movie = models.CharField(max_length=255)
    favorite_quote = models.TextField()

    def __str__(self):
        return self.name