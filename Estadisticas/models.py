from django.db import models

class Trofeo(models.Model):
    nombre = models.CharField(max_length=100)
    anio = models.IntegerField(help_text="Anio en que se obtuvo") # Cambiado Año -> Anio

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='escudos/', null=True, blank=True)
    trofeos = models.ManyToManyField(Trofeo, related_name='equipos', blank=True)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='jugadores/', null=True, blank=True)
    posicion = models.CharField(max_length=50)
    goles = models.PositiveIntegerField(default=0)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')

    def __str__(self):
        return self.nombre