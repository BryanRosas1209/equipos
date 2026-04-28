from django.db import models

class Liga(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Liga"
        verbose_name_plural = "Ligas"

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, default="Nombre provisional")
    ciudad = models.CharField(max_length=100, default="Ciudad desconocida")
    # Agregamos la relación con Liga
    liga = models.ForeignKey(Liga, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipos')

    def __str__(self):
        return self.nombre

# ... (Tus otros modelos Jugador, EstadisticaJugador, Trofeo se quedan igual)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100, default="Jugador Anónimo")
    posicion = models.CharField(max_length=50, default="Sin posición")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class EstadisticaJugador(models.Model):
    jugador = models.OneToOneField(Jugador, on_delete=models.CASCADE, related_name='estadisticas')
    partidos_jugados = models.PositiveIntegerField(default=0, verbose_name="PJ")
    goles = models.PositiveIntegerField(default=0, verbose_name="Goles")
    asistencias = models.PositiveIntegerField(default=0, verbose_name="Asistencias")
    tarjetas_amarillas = models.PositiveIntegerField(default=0, verbose_name="TA")
    tarjetas_rojas = models.PositiveIntegerField(default=0, verbose_name="TR")

    class Meta:
        verbose_name = "Estadística de Jugador"
        verbose_name_plural = "Estadísticas de Jugadores"

class Trofeo(models.Model):
    nombre = models.CharField(max_length=100)
    anio = models.PositiveIntegerField(verbose_name="Año", default=2026)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='trofeos')

    class Meta:
        verbose_name = "Título" # Aquí cambiamos el nombre para que salga como Títulos
        verbose_name_plural = "Títulos"

    def __str__(self):
        return f"{self.nombre} ({self.anio})"