
from django.shortcuts import render,redirect
from .models import Employee

def showIndex(request):
    return render(request,"index.html")

def savedetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    image = request.FILES["image"]
    Employee(idno=idno,name=name,salary=salary,image=image).save()
    #return render(request,"index.html",{"message":"Employee Created"})
    return redirect('/index/')

def viewAllEmployees(request):
    qs = Employee.objects.all()
    if qs:
        return render(request,"details.html",{"data":qs})
    else:
        return render(request,"details.html",{"message":"No Employee's are Available"})