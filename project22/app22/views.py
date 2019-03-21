from django.shortcuts import render
from .models import Employee

def showindex(request):
    return render(request,"index.html")


def empdetails(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    salary=request.POST.get("salary")
    image=request.FILES["image"]
    Employee(idno=idno,name=name,salary=salary,image=image).save()
    return render(request,"index.html",{"message":"employee details saved"})


def showAll(request):

    qs=Employee.objects.all()

    if qs:
        return render(request,"details.html",{"data":qs})
    else:
        return render(request,"details.html",{"message":"no employees in the database"})