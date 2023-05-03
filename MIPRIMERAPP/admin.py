from django.contrib import admin
from .models import Vuelo, Aeropuerto
# Register your models here.

admin.site.register(Vuelo)
class VueloNuevo(admin.ModelAdmin):
    list_display = ("id", "origen", "destino", "duracion")


admin.site.register(Aeropuerto)
class AeropuertoNuevo(admin.ModelAdmin):
    list_display = ("id", "codigo", "ciudad")