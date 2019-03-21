from django.shortcuts import render

def show(request):
    d1={
        101:{"name":"A", "class":10,"marks":[65,95,85,50,45,99],"total":sum([65,95,85,50,45,99])},
        102:{"name":"B", "class":11,"marks":[55,91,75,50,85,79]},
        103:{"name":"C", "class":12,"marks":[65,85,55,70,45,89]}}

    return render(request, "index.html", {"data": d1})