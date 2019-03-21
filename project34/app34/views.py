from django.shortcuts import render
from .models import Employee

def showIndex(request):
    return render(request,"index.html")


def saveDetails(request):
    id = request.POST.get("idno")
    name = request.POST.get("name")
    sal = request.POST.get("salary")
    e1 = Employee(idno=id,name=name,salary=sal)
    e1.save()
    return render(request,"index.html",{"message":"Data inserted"})


def showAll(request):
    qs = Employee.objects.all()
    return render(request,"details.html",{"data":qs})


def deleteEmployee(request):

    id = request.GET.get("id")
    Employee.objects.filter(idno=id).delete()

    #qs = Employee.objects.all()
    #return render(request,"details.html",{"data":qs})

    return render(request,"index.html")


def updateEmployee(request):
    id = request.POST.get("id")
    qs = Employee.objects.filter(idno=id)
    return render(request,"update.html",{"data":qs})


def updateEMP(request):
    id = request.POST.get("idno")
    name = request.POST.get("name")
    sal = request.POST.get("salary")
    e1 = Employee(idno=id, name=name, salary=sal)
    e1.save()
    return render(request, "index.html", {"message": "Data Updated"})

