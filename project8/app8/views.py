from django.shortcuts import render
from django.http import HttpResponse
def show(request):
    return render(request, "index.html")

def display(request):
    d1={
        "a":request.POST.get("t1"),
        "b":request.POST.get("t2"),
        "c":request.POST.get("t3"),
        "d":request.POST.get("t4"),
        "e":request.POST.get("t5"),
        "f":request.POST.get("t6")}


    return render(request, "details.html", d1)

def ok(request):
    return HttpResponse("<html> <body> <h1>Thank You registration successful</h1> </body> </html>")