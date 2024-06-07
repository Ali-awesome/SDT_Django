from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length= 25)
    bio = models.TextField()
    contact = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    