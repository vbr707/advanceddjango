from django.shortcuts import render

def show(request):
    return render(request, "index.html")
def details(request):

    data = request.POST.getlist("cb")
    return render(request,"details.html", {"data":data})