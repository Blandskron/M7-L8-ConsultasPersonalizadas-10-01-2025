# urls.py
from django.urls import path
from .views import listado_alumnos

urlpatterns = [
    path('alumnos/', listado_alumnos, name='listado_alumnos'),
]
