from django.db import models

# Create your models here.

class Teammate(models.Model):
    name = models.CharField(max_length=10)
    birth = models.DateField()
    home = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    major = models.CharField(max_length=20)
    studentnum = models.IntegerField()
    lover = models.CharField(max_length=10)
    food = models.CharField(max_length=20)
    alcohol = models.CharField(max_length=20)
    dream = models.TextField()