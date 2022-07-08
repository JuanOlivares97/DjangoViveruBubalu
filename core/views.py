from cgitb import html
from django.contrib import messages
from urllib import request
from django.forms import EmailField
from django.shortcuts import render, redirect
from carro.carro import Carro
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def suscribirse(request):
    usuario = nuevoUsuario.objects.get(Email=request.POST['correo'])
    if usuario.suscrito == True:
        messages.success(request,'Usted ya esta Suscrito')
    else:
        usuario.suscrito = False
        usuario.save()
    return redirect(to='home')


def eliminarProducto(request,id):
    producto = Producto.objects.get(id_producto=id)
    producto.delete()
    return redirect(to="listar_producto")

def eliminarPromocion(request,id):
    promocion = Promocion.objects.get(id_promocion=id)
    promocion.delete()
    return redirect(to="listar_promocion")

def paginaLogin(request):
    if request.method=='POST':
        try:
            detalleUsuario=nuevoUsuario.objects.get(Email=request.POST['correo'], pwd=request.POST['password'])
            print("Usuario= ",detalleUsuario)
            request.session['nombre']=detalleUsuario.nombre
            return redirect ('home')
        except nuevoUsuario.DoesNotExist as e:
            print('Email o contrasela incorrectos!')
    return render(request,'core/login.html')

def registroUsuario(request):
    if request.method == 'POST':
        if nuevoUsuario.objects.filter(Email = request.POST['correo']).exists(): 
            messages.success(request, 'El email ingresado ya esta registrado')
        else:
            correo=request.POST['correo']
            pwd=request.POST['password']
            nombre=request.POST['firstName']
            apellido=request.POST['lastName']
            nuevoUsuario(Email=correo, pwd=pwd, nombre=nombre, apellidos=apellido).save()
            messages.success(request, 'El usuario '+request.POST['firstName']+' se registró correctamente.')
            return redirect('paginaLogin')
    return render(request, 'core/register.html')


def cerrarSesion(request):
    try:
        del request.session['nombre']
    except:
        print("Paso algo..")
        return render(request, 'core/home.html')
    return redirect ('home')


def modificar_promocion(request,id):
    promocion = Promocion.objects.get(id_promocion=id)
    datos = {"form":promocionForm(instance=promocion)}
    if request.method == "POST":
        form = promocionForm(request.POST, instance=promocion)
        if form.is_valid:
            form.save()
            datos['form'] = form
    return render(request, 'core/modificar_promocion.html',datos)


def modificar_producto(request,id):
    producto = Producto.objects.get(id_producto=id)
    datos = {"form":productoForm(instance=producto)}
    if request.method == "POST":
        form = productoForm(request.POST, instance=producto)
        if form.is_valid:
            form.save()
            datos['form'] = form
    return render(request, 'core/modificar_producto.html',datos)

def carro(request):
    carro=Carro(request)
    return render(request, 'core/carro.html')

def listar_promocion(request):
    contexto = {'promociones' : Promocion.objects.all()}
    return render(request,'core/listar_promocion.html',contexto)

def listar_producto(request):
    contexto = {'productos': Producto.objects.all()}
    producto = Producto.objects.order_by('id_producto')
    return render(request, 'core/listar_producto.html', contexto)

def agregar_productos(request):
    datos = {'form':productoForm()}
    if request.method == 'POST':
        formulario = productoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            datos["mensaje"] = "Guardado Correctamente"
        else:
            datos["form"] = formulario
    return render(request, 'core/agregar_productos.html',datos)


def agregar_promocion(request):
    datos = {'form':promocionForm()}
    if request.method == 'POST':
        formulario = promocionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            datos["mensaje"] = "Guardado Correctamente"
        else:
            datos["form"] = formulario
    return render(request, 'core/agregar_promocion.html',datos)
    
def ingresar(request):
    return render(request, 'core/login.html')


def historial_compras(request):
    return render(request, 'core/historial_compras.html')

def registro(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect(to="login")
    else:
        return render(request, 'core/registro.html', {'form':UserCreationForm()})

def home(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'core/home.html', contexto)





def eliminarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to="home")
    