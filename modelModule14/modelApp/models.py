from django.db import models

# Create your models here.

class Person(models.Model):
    userId = models.IntegerField(primary_key= True,default= 1)
    userName = models.CharField(max_length=25)
    userEmail = models.EmailField(unique=True)
    userPassword = models.CharField(max_length=10)

    def __str__(self):
        return f"Roll: {self.userId} - {self.userName}"