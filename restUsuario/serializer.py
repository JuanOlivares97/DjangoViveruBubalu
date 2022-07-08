from rest_framework.serializers import ModelSerializer
from core.models import *

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = nuevoUsuario
        fields = ['nombre', 'apellidos', 'Email', 'pwd', 'suscrito'] 


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nom_producto', 'stock', 'precio', 'img_producto']


class PromocionSerializer(ModelSerializer):
    class Meta:
        model = Promocion
        fields = ['id_promocion','nom_promocion','porcentaje','fecha_ini','fecha_termino']
