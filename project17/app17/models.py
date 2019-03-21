from django.db import models

class employee(models.Model):
    idno= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=30)
    age= models.IntegerField()
    actual_salary= models.DecimalField(max_digits=10,decimal_places=2)
    designation=models.CharField(max_length=20)
    shift=models.CharField(max_length=20)
    loans=models.CharField(max_length=10)
    net_salary=models.DecimalField(max_digits=10,decimal_places=2)