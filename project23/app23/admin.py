from django.contrib import admin
from .models import Employee
from .models import User

# Register your models here.
admin.site.register(Employee)
admin.site.register(User)

#https://docs.djangoproject.com/en/2.1/intro/tutorial02/