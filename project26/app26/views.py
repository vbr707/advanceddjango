from django.shortcuts import render,HttpResponse
from .models import Employee
import csv
# Create your views here.
def show(request):
    return render(request,'index.html')

def downloadCSVDB(requast):
    res = HttpResponse(content_type="text/csv")
    res['Content-Disposition']='attachments;filename="sampleDB.csv"'
    write = csv.writer(res)
    qs=Employee.objects.all()
    for x in qs:
        write.writerow([x.idno,x.name,x.salary])
    return res

