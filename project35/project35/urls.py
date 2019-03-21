"""project35 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app35 import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.showMenu.as_view(),name='menu'),
    path('home/', views.TemplateView.as_view(template_name="home.html"),name='home'),
    path('myadmin/', views.TemplateView.as_view(template_name='admin.html'),name='myadmin'),
    path('employee/', views.TemplateView.as_view(template_name='employee.html'),name='employee'),
    path('user/', views.TemplateView.as_view(template_name='user.html'),name='user')
]
