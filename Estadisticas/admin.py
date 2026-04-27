from django.contrib import admin
from .models import Equipo, Jugador, Trofeo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad') # Columnas que verás en la lista
    search_fields = ('nombre',)        # Barra de búsqueda

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'equipo', 'goles')
    list_filter = ('equipo', 'posicion') # Filtros laterales

@admin.register(Trofeo)
class TrofeoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'anio')