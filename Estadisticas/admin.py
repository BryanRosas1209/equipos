from django.contrib import admin
from .models import Equipo, Jugador, EstadisticaJugador, Trofeo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad')

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'equipo')

@admin.register(Trofeo)
class TrofeoAdmin(admin.ModelAdmin):
    # Esta es tu sección de Títulos / Palmarés
    list_display = ('nombre', 'anio', 'equipo')
    list_filter = ('equipo',)

@admin.register(EstadisticaJugador)
class EstadisticaJugadorAdmin(admin.ModelAdmin):
    list_display = ('jugador', 'goles', 'asistencias', 'partidos_jugados')