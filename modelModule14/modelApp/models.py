from django.db import models

# Create your models here.

class Person(models.Model):
    userName = models.CharField(max_length=25)
    userEmail = models.EmailField(unique=True)
    userPassword = models.CharField(max_length=10)