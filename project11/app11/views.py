from django.shortcuts import render

def showindex(request):
    return render(request, "index.html")
def showdetails(request):

    cb=request.POST.getlist("cb")
    data={"Movies":['GULLY BOY','Alita:Battle Angel','The Surgical Strike','Dev','Manikarnika'],
          "Cartoons":['Bugs Bunny','Mickey Mouse','Tweety','Popeye','Daffy Duck'],
          "Images":['.JPG','.PNG','.GIF','.BMP','.TIFF']}

    return render(request,"details.html",{"cb":cb,"data":data})
