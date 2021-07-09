from django.http import request
from core.admin import RopaAdmin
from core.models import DescripcionRopa
from django.shortcuts import render
from core.models import TipoRopa
from .forms import RopaForm
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    return render(request, 'core/registro.html')

def producto(request):
    ropass = DescripcionRopa.objects.all()

    data = {
         'ropass' : ropass
     }
    return render(request, 'core/productos.html', data)


@login_required
@permission_required('core.add_')
def nuevo_producto(request): 
    
    formulario = RopaForm(request.POST or None)
    contexto = {
        'form' : formulario
    }
    if formulario.is_valid():
        formulario.save()
        contexto ['mensaje'] = "Guardado correctamente"

    
    return render(request, 'core/nuevo_producto.html', contexto)
@login_required
def modificar_producto(request, id):
    producto = DescripcionRopa.objects.get(id=id)
    data = {
        'form':RopaForm(instance=producto)
    }

    if request.method =='POST':
        formulario = RopaForm(data=request.POST, instance= producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['forma'] = formulario
    return render(request, 'core/modificar_producto.html', data)

@login_required
def eliminar_producto(request, id):
    producto = DescripcionRopa.objects.get(id=id)
    producto.delete()

    return redirect(to="productos")
        

