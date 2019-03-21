from django.shortcuts import render
from django.http import HttpResponse
from .models import PostGet
# Create your views here.
def index(request):
    return render(request,"index.html")



def postExample(request):
    un=request.POST.get("pname")
    up=request.POST.get("ppassword")
    PostGet(un=un,up=up).save()
    return HttpResponse("your details posted via post method")

def getExample(request):
    un = request.GET.get("pname")
    up = request.GET.get("ppassword")
    PostGet(un=un,up=up).save()
    return HttpResponse("your details send via get method")

