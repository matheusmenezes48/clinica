from django.shortcuts import render
from . models import Cliente, Medico

def home(request):
    return render(request, 'home.html',{})


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request,'cliente/list.html',{'clientes':clientes})

def cliente_show(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request,'cliente/show.html',{'cliente':cliente})

def cliente_create(request):
    return render(request,'cliente/form.html')

def medico_list(request):
    medicos = Medico.objects.all()
    return render(request,'medico/list.html',{'medicos':medicos})

def medico_show(request, medico_id):
    medico = Medico.objects.get(pk=medico_id)
    return render(request,'medico/show.html',{'medico':medico})

