import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_editor = models.BooleanField(default=False)

    # Agregamos estos related_name para evitar el choque de nombres
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='estadisticas_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='estadisticas_user_permissions',
        blank=True
    )

# 🏆 Liga (Como tus Categorías)
class Liga(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, unique=True)
    pais = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "Ligas"

    def __str__(self):
        return self.nombre

# 🛡️ Equipo
class Equipo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    liga = models.ForeignKey(Liga, on_delete=models.SET_NULL, null=True, related_name='equipos')

    def __str__(self):
        return self.nombre

# 🏃 Jugador
class Jugador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=150)
    posicion = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')

    def __str__(self):
        return self.nombre

# 📅 Partido (Nuevo concepto clave)
class Partido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    torneo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha.strftime('%d/%m/%y')}"

# 📊 Desempeño (Esta es tu tabla intermedia estilo "CartItem")
class EstadisticaPartido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='rendimiento_partidos')
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='estadisticas')
    
    goles = models.PositiveIntegerField(default=0)
    asistencias = models.PositiveIntegerField(default=0)
    amarillas = models.PositiveIntegerField(default=0)
    rojas = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('jugador', 'partido') # Evita duplicar datos del mismo jugador en un partido

# 🥇 Título / Trofeo
class Trofeo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='trofeos')

    def __str__(self):
        return f"{self.nombre} ({self.anio})"