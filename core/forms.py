from pyexpat import model

from django.forms import ModelForm
from .models import Producto, Promocion, Vehiculo

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'categoria']

class productoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class promocionForm(ModelForm):
    class Meta:
        model = Promocion
        fields = '__all__'