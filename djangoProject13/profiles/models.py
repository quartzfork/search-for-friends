from django.db import models


class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    INSTITUTE_CHOICES = [
        ('IMKT', 'ИМКТ'),
        ('IMO', 'ИМО'),
        ('PI', 'ПИ'),
        ('SHIGN', 'ШИГН'),
        ('SHP', 'ШП'),
        ('SHM', 'ШМ'),
        ('SHEM', 'ШЭМ'),
        ('VISHRIMI', 'ВИШРИМИ'),
    ]
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Пол")
    institution = models.CharField(max_length=10, choices=INSTITUTE_CHOICES, verbose_name="Институт")
    telegram_username = models.CharField(max_length=100, blank=True, null=True, verbose_name="Имя в телеграмм")
    interests = models.TextField(verbose_name="Инетересы или обо мне")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
