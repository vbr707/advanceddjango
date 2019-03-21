from django.shortcuts import render

def showindex(request):
    return render(request,"index.html")

def media(request):
    cb=request.POST.getlist("cb")
    if cb==[]:
        return render(request,"index.html",{"data":"please select any one option"})
    else:
        data={"kgf":['image','audio'],"dev":['image','audio']}
        if len(data)==[1]:
        return render(request, "media.html", {"data":data,"cb":cb})