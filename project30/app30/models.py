from django.db import models

# Create your models here.
class Login(models.Model):
    un=models.CharField(max_length=30,primary_key=True)
    up=models.CharField(max_length=20)
class Feedback(models.Model):
    un = models.CharField(max_length=30)
    message = models.TextField()