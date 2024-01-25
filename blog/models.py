from django.db import models

# Create your models here.

class Menu (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='menu/img')
    bio = models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    img = models.ImageField(upload_to='team/img')

    def __str__(self):
        return self.name