from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.contrib.auth.models import User
from django.http import HttpResponse



def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/formulario.html', {'form': form})

def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    form = TareaForm(request.POST or None, instance=tarea)
    if form.is_valid():
        form.save()
        return redirect('lista_tareas')
    return render(request, 'tareas/formulario.html', {'form': form})

def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    return render(request, 'tareas/eliminar.html', {'tarea': tarea})

def crear_superusuario(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse("✅ Superusuario creado: admin / admin123")
    else:
        return HttpResponse("⚠️ Ya existe un superusuario con ese nombre.")