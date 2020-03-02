"""wedding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic.base import TemplateView
from app_wedding import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('alojamientos', TemplateView.as_view(template_name='alojamientos.html')),
    path('ubicacion', TemplateView.as_view(template_name='ubicacion.html')),
    path('organizacion', TemplateView.as_view(template_name='organizacion.html')),
    path('regalo-boda', TemplateView.as_view(template_name='regalo-boda.html')),
    path('peluquerias', TemplateView.as_view(template_name='peluquerias.html')),
    path('manicura', TemplateView.as_view(template_name='manicura.html')),
    path('confirmacion', views.ContactFormView.as_view()),
]
