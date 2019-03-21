from django.shortcuts import render
from django.views.generic import RedirectView


# Create your views here.
class OpenFB(RedirectView):
    url = "http://www.facebook.com"


#class showindex(TemplateView):
 #   template_name = "index.html"