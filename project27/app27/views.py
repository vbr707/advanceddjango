from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .models import Employee
# Create your views here.
def download(request):

    return render(request,"index.html")


def pdf(request):
    res=HttpResponse(content_type="application/pdf")
    res['Content-Disposion']='attachment,filename="employee-details.pdf"'
    pdf=canvas.Canvas(res)
    qs=Employee.objects.all()
    y=800
    for x in qs:
        data=str(x.idno)+"   "+x.name+"   "+str(x.salary)
        pdf.drawString(0,y,data)
        y-=150
        print(y)
    pdf.showPage()
    pdf.save()
    return res