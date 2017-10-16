from django.db import models
from django.contrib.auth.models import User


class Cat(models.Model):
    owner = models.ForeignKey(User, related_name='cats', default=None)
    birthday = models.DateTimeField()
    name = models.CharField(max_length=100)

class Dog(models.Model):
    owner = models.ForeignKey(User, related_name='dogs', default=None)
    birthday = models.DateTimeField()
    name = models.CharField(max_length=100)
