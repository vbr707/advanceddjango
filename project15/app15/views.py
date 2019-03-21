from django.shortcuts import render

def showindex(request):
    return render(request,"index.html")
def show(request):
    rd=request.POST.get("rd")
    global username
    username=request.POST.get("na")
    password=request.POST.get("pwd")

    if rd=="admin":
        if username=="ravi" and password=="Ravi@123":
            return render(request,"admin.html",{"username":username})
        else:
            return render(request,"index.html",{"err_mess":"invalid username or password"})
    elif rd=="emp":
        if username=="kumar" and password=="kumar":
            return render(request,"emp.html",{"username":username})
        elif username=="mohan" and "krishna":
            return render(request,"emp.html",{"username":username})
        elif username=="prasad" and password=="deepak":
            return render(request,"emp.html",{"username":username})
        else:
            return render(request,"index.html",{"err_mess":"invalid username or password"})
    else:
        if username=="naveen" and password=="kumar#99":
            return render(request,"user.html",{"username":username})
        elif username=="rama" and password=="rani":
            return render(request,"user.html",{"username":username})
        else:
            return render(request,"index.html",{"err_mess":"invalid username or password"})

def valid(request):
    uid=int(request.POST.get("uid"))
    if uid==6557:
        return render(request,"emp1.html",{"username":username,"uid":uid})
    elif uid==3128:
        return render(request, "emp1.html", {"username":username,"uid": uid})
    elif uid==707:
        return render(request, "emp1.html", {"username":username,"uid": uid})
    else:
        return render(request, "emp.html",{"err_mess":"ivalid uid"})