from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.TextField(max_length=40)
    age = models.IntegerField(default=1)
    color = models.TextField(max_length=60)
    for_adoption = models.BooleanField()

class Rescue(models.Model):
    pass