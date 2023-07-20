from django.shortcuts import render
from .models import Familiar

def crear_familiares_de_prueba():
    Familiar.objects.create(numero=1, cadena='Familiar 1', fecha='2023-01-01')
    Familiar.objects.create(numero=2, cadena='Familiar 2', fecha='2023-02-01')
    Familiar.objects.create(numero=3, cadena='Familiar 3', fecha='2023-03-01')

def listar_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'familiares/listar.html', {'familiares': familiares})
