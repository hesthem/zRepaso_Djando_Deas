from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DEA
from .queries import *
import utm

def index(request):
    if request.method == "POST":
        latitud = float(request.POST["lat"])
        longitud = float(request.POST["lng"])
        deas = DEA.objects.all()
        dea, url = nearest_dea(latitud, longitud, deas)
        context = {"dea": dea, "url": url}
        return render(request, "finder/index.html", context)
    else:
        return render(request, "finder/user.html")

def listado(request):
    deas = DEA.objects.all()[0:100]
    context = {"deas": deas}
    return render(request, "finder/listado.html", context)

def contact(request):
    # deas = data
    # insert_into(deas)
    return HttpResponse("Se encuentra en la página de contactos")

def user(request):
    return render(request, "finder/user.html")

def details(request):
    if request.method == "POST":
        codigo_dea = request.POST["codigo_dea"]
        dea = DEA.objects.filter(codigo_dea=codigo_dea)[0]
        dea_latlng = utm.to_latlon(dea.x_utm, dea.y_utm, 30, "N")
        url = f"https://www.google.com/maps/search/?api=1&query={dea_latlng[0]},{dea_latlng[1]} "
        context = {"dea": dea, "url": url}
        return render(request, "finder/details.html", context)
    else:
        return redirect("/listado")
