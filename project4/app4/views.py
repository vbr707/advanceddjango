from django.shortcuts import render


def show(request):
    d1={
        "emp_idno":101,
        "name":"raju",
        "salary":125000.00,
        "status": True
    }
    return render(request,"index.html",d1)