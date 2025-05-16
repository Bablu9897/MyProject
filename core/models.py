from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    points = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

class App(models.Model):
    name = models.CharField(max_length=100)
    package = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='app_icons/')
    points = models.PositiveIntegerField()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    completed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)