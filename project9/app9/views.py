from django.shortcuts import render

def show(request):
    return render(request,"index.html")

def display(request):
     name = request.POST.get("t1")
     pwd =request.POST.get("t2")

     if(name =="Ravi" and pwd =="kumar123"):
         result = "valid"
     else:
         result = "invalid"

     return render(request,"index.html",{"result":result})