from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import *

# Create your views here.
class lista(ListView):
    model= Curso
    template_name='index.html'
def eliminacion(request,id):
    curso=Curso.objects.get(id=id)
    curso.delete()
    return redirect('/')
def registrarcurso(request):
    nombre=request.POST['txtnombre']
    creditos=request.POST['txtnum']
    curso=Curso.objects.create(nombre=nombre,creditos=creditos)
    return redirect('/')
def editar(request,id):
    curso=Curso.objects.get(id=id)
    data={
        'titulo':'edicion del curso',
        'curso':curso
    }
    return render(request,'edicion.html',data)
def editarcurso(request):
    id=int(request.POST['id'])
    nombre=request.POST['txtnombre']
    creditos=request.POST['txtnum']
    
    curso=Curso.objects.get(id=id)
    curso.nombre=nombre
    curso.creditos=creditos
    curso.save()
    return redirect('/')