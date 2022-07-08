from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('registrar', registroUsuario, name="registroUsuario"),
    path('listar_producto', listar_producto, name="listar_producto"),
    path('listar_promocion', listar_promocion, name="listar_promocion"),
    path('login', paginaLogin , name="paginaLogin"),
    path('historial_compras', historial_compras, name="historial_compras"),
    path('agregar_productos', agregar_productos,name="agregar_productos"),
    path('modificar_producto/<id>', modificar_producto,name="modificar_producto"),
    path('agregar_promocion', agregar_promocion,name="agregar_promocion"),
    path('modificar_promocion/<id>', modificar_promocion,name="modificar_promocion"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
    path('eliminarPromocion/<id>', eliminarPromocion, name="eliminarPromocion"),
    path('carro',carro,name="carro"),
    path('cerrarSesion',cerrarSesion,name="cerrarSesion"),


]
