from django.shortcuts import render,redirect

# Create your views here.
def showIndex(request):
    return render(request,"index.html")

from .models import Login
def welcome(request):
   # un = request.session["un"]
  #  if un:
   #    return render(request,"welcome.html",{"massage":"welcome to sessions"})
  #  else:
        un = request.POST.get("username")
        up = request.POST.get("password")
        qs = Login.objects.filter(un=un,up=up)
        if qs:
            request.session["un"] = un  # Writing username to Sessions table
            return render(request, "welcome.html", {"message": "Welcome User"})
        else:
            return render(request, "index.html", {"message": "Invalid User"})
from .models import Feedback
def feedback(request):
    message = request.POST.get("fb")
    un = request.session["un"] # Reading username from sessions Table
    Feedback(un=un,message=message).save()

    return redirect("/logincheck/")

