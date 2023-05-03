from django.shortcuts import render
from django.http import HttpResponse
from .models import Vuelo, Aeropuerto

# Create your views here.

def index(request):

    return HttpResponse("Hola mundo, estas en la pagina principal de la app")

def about(request):
    if request.method == "GET":
        # definiendo el contexto
        context = {
        "vuelos":  Vuelo.objects.all(),
        "aeropuerto": Aeropuerto.objects.all(),
        }
        return render(request, "MIPRIMERAPP/about.html", context)
    else:   
        # extraer valores de la request
        origen = request.POST["origen"]
        destino = request.POST["destino"]

        print(request.POST)

        # obtener valores
        o = Aeropuerto.objects.get(codigo=origen)
        d = Aeropuerto.objects.get(codigo=destino)
        
        vuelos = Vuelo(
            origen = o,
            destino = d
        )
        vuelos.save()

        return render(request, "MIPRIMERAPP/about.html", {"vuelos": Vuelo.objects.all(), "aeropuerto": Aeropuerto.objects.all()})


def aeropuerto(request):
    if request.method == "GET":
        return render(request, "MIPRIMERAPP/aeropuerto.html", {"aeropuerto": Aeropuerto.objects.all()})
    else:
        codigo = request.POST["codigo"]
        ciudad = request.POST["ciudad"]
        print(request.POST)
        a = Aeropuerto(
            codigo = codigo,
            ciudad = ciudad
        )
        a.save()
        return render(request, "MIPRIMERAPP/aeropuerto.html", {"aeropuerto": Aeropuerto.objects.all()})