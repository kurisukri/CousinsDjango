from django.contrib import admin
from django.urls import path
from .views import eliminar_producto, index, login, modificar_producto, registro, producto, nuevo_producto

urlpatterns =[
    path('', index , name="index"),
    path('login/', login , name="login"),
    path('registro/', registro , name="registro"),
    path('productos/', producto, name="productos"), #listado
    path('nuevo_producto/', nuevo_producto, name="nuevo_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto")
]

admin.site.site_header = "Administración de Cousins"