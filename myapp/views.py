from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from . import models


def home(request):
    return render(request, 'base')


def todo(request):
    elementos = models.Todo.objects.all().order_by("-fechaCreado")
    return render(request, 'myapp/index.html', {
        "elementos": elementos,
    })


def agregar_elemento(request):
    fechaCreada = timezone.now()
    contenido = request.POST["contenido"]
    models.Todo.objects.create(fechaCreado=fechaCreada, texto=contenido)
    return HttpResponseRedirect("/")

def borrar_elemento(request, elemento_id):
    models.Todo.objects.get(id=elemento_id).delete()
    return HttpResponseRedirect("/")