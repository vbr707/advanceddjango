from django.db import models

# Create your models here.
class PostGet(models.Model):
    un=models.CharField(max_length=20)
    up=models.CharField(max_length=20)