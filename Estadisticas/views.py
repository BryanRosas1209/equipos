from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from .models import Equipo, Partido

def home(request):
    # Obtenemos todos los equipos registrados en la base de datos
    equipos = Equipo.objects.all()
    # Obtenemos los últimos 5 partidos jugados para mostrar resultados recientes
    partidos = Partido.objects.all().order_by('-fecha')[:5]
    
    return render(request, 'Estadisticas/home.html', {
        'equipos': equipos,
        'partidos': partidos
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente tras registrarse
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'Estadisticas/register.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = "Usuario o contraseña incorrectos" # <--- Notificamos el error
            
    return render(request, 'Estadisticas/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')