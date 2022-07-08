from django.urls import path
from .views import *

app_name="servicioRest"

urlpatterns=[
    path('usuarios', getUsuarios, name= "usuarios"),
    path('productos', getProducto, name= "productos"),
    path('promociones', getPromocion, name= "promociones"),
]
