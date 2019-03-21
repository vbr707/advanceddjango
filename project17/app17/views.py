from django.shortcuts import render

def emp(req):
    return render(req,"index.html")
def save(req):
     idno= req.POST.get("idno")
     name= req.POST.get("name")
     age= req.POST.get("age")
     salary= req.POST.get("salary")
     desig =req.POST.get("desig")
     r =req.POST.get("r")
     cb =req.POST.get("cb")


     return render(req,"index.html",{"idno":idno,"name":name,"age":age,"salary":salary,"desig":desig,"r":r,"cb":cb})
