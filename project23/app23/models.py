from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=20)
    salary =models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='emoloyee/')

    def __str__(self):
         return self.name
class User(models.Model):
    idno = models.AutoField(primary_key= True)
    name = models.CharField(max_length=20)
    contact = models.IntegerField()
    dob = models.DateField()
    image=models.ImageField(upload_to='user/')
    def __str__(self):
        return self.name