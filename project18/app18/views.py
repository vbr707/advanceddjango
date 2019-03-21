from django.shortcuts import render
from .models import employee
def showindex(req):
    return render(req,"index.html")


def save(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    age = request.POST.get("age")
    salary =float(request.POST.get("salary"))
    desig = request.POST.get("desig")
    r = request.POST.get("r")
    cb = request.POST.getlist("cb")

    if len(cb)==1 and 'no loan' in cb:
        e = employee(idno=idno, name=name, age=age, actual_salary=salary, designation=desig, shift=r, loans=cb,
                     net_salary=salary)
        e.save()
        return render(request, "index.html",
                      {"message": "details saved succesfully"})

    elif len(cb)==1 and 'Car' in cb:
        net_salary=salary-12500
        e = employee(idno=idno, name=name, age=age, actual_salary=salary, designation=desig, shift=r, loans=cb,
                     net_salary=net_salary)
        e.save()
        return render(request, "index.html",
                      {"message": "details saved succesfully"})
    elif len(cb)==1 and 'Home' in cb:
        net_salary=salary-30000
        e = employee(idno=idno, name=name, age=age, actual_salary=salary, designation=desig, shift=r, loans=cb,
                     net_salary=net_salary)
        e.save()
        return render(request, "index.html",
                      {"message": "details saved succesfully"})
    elif len(cb)==1 and 'Personal' in cb:
        net_salary=salary-7000
        e = employee(idno=idno, name=name, age=age, actual_salary=salary, designation=desig, shift=r, loans=cb,
                     net_salary=net_salary)
        e.save()
        return render(request, "index.html",
                      {"message": "details saved succesfully"})

    elif len(cb)==2 and 'Car''Home' in cb:
        net_salary=salary-12500-30000
        e = employee(idno=idno, name=name, age=age, actual_salary=salary, designation=desig, shift=r, loans=cb,
                     net_salary=net_salary)
        e.save()
        return render(request, "index.html",
                      {"message": "details saved succesfully"})
    elif len(cb)==2 and 'Car''Personal' in cb:
        net_salary=salary-12500-7000
        e = employee(idno=idno, name=name, age=age, actual_salary=salary, designation=desig, shift=r, loans=cb,
                 net_salary=net_salary)
        e.save()
        return render(request, "index.html", {"message": "your details saved succesfully"})

    elif len(cb)==2 and 'Home''Personal' in cb:
        net_salary=salary-30000-7000
        e = employee(idno=idno, name=name, age=age, actual_salary=salary, designation=desig, shift=r, loans=cb,
                     net_salary=net_salary)
        e.save()
        return render(request, "index.html", {"message": "your details saved succesfully"})
    else:
        net_salary=salary-12500-30000-7000
        e = employee(idno=idno, name=name, age=age, actual_salary=salary, designation=desig, shift=r, loans=cb,
                     net_salary=net_salary)
        e.save()
        return render(request, "index.html",
                      {"message":"details saved succesfully"})

