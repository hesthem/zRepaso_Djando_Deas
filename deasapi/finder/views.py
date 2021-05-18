from django.shortcuts import render
from django.http import HttpResponse
from .queries import *
# Create your views here.

def index(request):
    return render(request, "finder/index.html")

def contact(request):
    return HttpResponse("Se encuentra en la página de contacto")