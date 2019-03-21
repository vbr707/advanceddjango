from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def setCookie(request):
    res=HttpResponse("the cookie is set")
    res.set_cookie("name","raju")
    return res

def getCookie(request):
    res=request.COOKIES["name"]
    response=HttpResponse("the cookie is :"+res)
    return response