from django.db import models

class Trofeo(models.Model):
    # ... tus campos ...
    class Meta:
        verbose_name = "Trofeo"
        verbose_name_plural = "Trofeos"

class Equipo(models.Model):
    # ... tus campos ...
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

class Jugador(models.Model):
    # ... tus campos ...
    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

    def __str__(self):
        return self.nombre