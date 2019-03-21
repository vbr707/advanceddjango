from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

def showIndex(request):
    return render(request,"index.html")
class MyCBV(View):
    def post(self,request):
        return HttpResponse("post clicked")
    def get(self,request):
        return HttpResponse("get clicked")
