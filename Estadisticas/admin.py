from django.contrib import admin
from .models import Equipo, Jugador, EstadisticaJugador, Trofeo, Liga

@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    # Ahora mostramos la liga en la lista de equipos
    list_display = ('nombre', 'ciudad', 'liga')
    list_filter = ('liga',) # Filtro lateral por liga
    search_fields = ('nombre',)

# ... (El resto de tus registros Admin se quedan igual)

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