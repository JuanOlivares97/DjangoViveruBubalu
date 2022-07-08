from django.urls import path
from .import views

app_name="carrito"

urlpatterns = [
    path('agregar/<int:id>/', views.agregar_producto,name="agregar"),
    path('eliminar/<int:id>/', views.eliminar_producto,name="eliminar"),
    path('restar/<int:id>/', views.restar_producto,name="restar"),
    path('limpiar', views.limpiar_carro,name="limpiar"),
]