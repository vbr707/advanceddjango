from django.shortcuts import render

def show(request):
    d1={
        "101":{"name":"ravi", "salary":125000.00},
        "102":{"name":"kumar", "salary":185000.00},
        "103":{"name":"mohan", "salary":200000.00}}
    return render(request, "index.html", {"data": d1})
