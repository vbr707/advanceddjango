from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class showMenu(TemplateView):
    template_name = "menu.html"