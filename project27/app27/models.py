from django.db import models

# Create your models here.
class Employee(models.Model):
    idno=models.IntegerField(primary_key=True,default=False)
    name=models.CharField(max_length=20)
    salary=models.DecimalField(max_digits=10,decimal_places=2)