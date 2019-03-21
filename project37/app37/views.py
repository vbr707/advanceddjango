from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Employee


# Create your views here.
class viewAllEmployees(ListView):
    model = Employee
    template_name = "viewall.html"


class viewIdSal(ListView):
    model = Employee
    template_name = "viewidsal.html"
    queryset = Employee.objects.values('salary', 'idno')


class viewId(ListView):
    model = Employee
    queryset = Employee.objects.values('idno')
    template_name = "onlyid.html"
