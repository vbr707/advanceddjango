from django.shortcuts import render

from app19.models import Employee


def showInex(request):
    return render(request,"index.html")


def empdetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    d={
        "idno":idno,
        "name":name,
        "salary":salary
    }
    if d:
        Employee(idno=idno,name=name,salary=salary).save()
        return render(request,"index.html",{"data":d})
    else:
        return render(request,"index.html",{"data":"please enter emp details"})