from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showhlinks(request):
    return render(request,"hlinks.html")


def postExample(request):
    return render(request,"index.html")


def getExample(request):
    return render(request,"index.html")

from .models import PostGet
def pcheck(request):
    un = request.POST.get("pname")
    up= request.POST.get("ppassword")
    qs=PostGet.objects.filter(un=un,up=up)
    if qs:
        return HttpResponse("yes,post method working securely")
    else:
        return HttpResponse("no,data found for post")

def gcheck(request):
    un =request.GET.get("gname")
    up =request.GET.get("gpassword")
    qs=PostGet.objects.filter(un=un,up=up)
    if qs:
        return HttpResponse("yes,get method working non secure and visiible username & password in url search bar")
    else:
        return HttpResponse("no,data found for get")