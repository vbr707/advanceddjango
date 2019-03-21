from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def checMethodType(request):
    if request.method=="POST":
        return HttpResponse("post clicked")
    if request.method=="GET":
        return HttpResponse("get clicked")