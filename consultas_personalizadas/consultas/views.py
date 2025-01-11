from django.shortcuts import render
from .models import Alumno

def listado_alumnos(request):
    # Obtener todos los alumnos de la base de datos
    alumnos = Alumno.objects.all()
    
    # Renderizar el template 'alumnos.html' con los datos
    return render(request, 'consultas/alumnos.html', {'alumnos': alumnos})
