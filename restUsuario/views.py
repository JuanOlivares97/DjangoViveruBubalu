from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from core.models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getUsuarios(request):
    if request.method == 'GET':
        usuarios = nuevoUsuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'PUT':
        usuarios = nuevoUsuario.objects.filter(Email = id).first()
        serializer = UsuarioSerializer(usuarios, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        usuarios = nuevoUsuario.objects.filter(Email=id).first()
        usuarios.delete()
        return Response('Eliminado')


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getProducto(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'PUT':
        productos = Producto.objects.filter(id_producto = id).first()
        serializer = ProductoSerializer(productos, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        productos = Producto.objects.filter(id_producto=id).first()
        productos.delete()
        return Response('Eliminado')

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getPromocion(request):
    if request.method == 'GET':
        promociones = Promocion.objects.all()
        serializer = PromocionSerializer(promociones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PromocionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'PUT':
        promociones = Producto.objects.filter(id_promocion = id).first()
        serializer = PromocionSerializer(promociones, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        promociones = Producto.objects.filter(id_promocion=id).first()
        promociones.delete()
        return Response('Eliminado')


