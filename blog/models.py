from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Articles(models.Model):
    title = models.CharField(max_length = 200)
    details = models.CharField( max_length = 9000 )
    date = models.DateField(auto_now_add  = True)
    status = models.BooleanField(default = True)
    def __str__(self):
        return f"{self.title}"

class Lectures(models.Model):
    title = models.CharField(max_length = 200)
    lecture = models.FileField(upload_to = 'lectures/', max_length=100)
    description = models.CharField(max_length = 2000)
    date = models.DateField(auto_now_add  = True)
    status = models.BooleanField(default = True)
    def __str__(self):
        return f"{self.title}"

class Gallery(models.Model):
    title = models.CharField(max_length = 200)
    picture = models.ImageField(upload_to = 'gallery/')
    date = models.DateField(auto_now_add = True)
    status = models.BooleanField(default = True)
    def __str__(self):
        return f"{self.title}"
