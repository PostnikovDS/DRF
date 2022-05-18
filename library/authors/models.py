from django.db import models


class Author(models.Model):
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    birthday = models.PositiveSmallIntegerField()


class User(models.Model):
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    birthday = models.PositiveSmallIntegerField()
    email = models.CharField('Электронная почта', max_length=64, unique=True)
    