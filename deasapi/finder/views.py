from django.shortcuts import render
from django.http import HttpResponse
from .models import DEA
from .queries import *

def index(request):
    deas = DEA.objects.all()
    dea, url = nearest_dea(40.39752815757715, -3.716253259298705, deas)
    context = {"dea": dea, "url": url}
    return render(request, "finder/index.html", context)

def listado(request):
    deas = DEA.objects.all()
    context = {"deas": deas}
    return render(request, "finder/listado.html", context)

def contact(request):
    # deas = data
    # insert_into(deas)
    return HttpResponse("Se encuentra en la página de contactos")