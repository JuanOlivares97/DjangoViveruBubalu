from django.shortcuts import render
from .carro import Carro
from core.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request,id):
    carro = Carro(request)
    producto=Producto.objects.get(id_producto=id)
    carro.agregar(producto=producto)
    return redirect("carro")

def eliminar_producto(request, id):
    carro = Carro(request)
    producto=Producto.objects.get(id_producto=id)
    carro.eliminar(producto=producto)
    return redirect("carro")

def restar_producto(request, id):
    carro = Carro(request)
    producto=Producto.objects.get(id_producto=id)
    carro.restar_producto(producto=producto)
    return redirect("carro")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("carro")