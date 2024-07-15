from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Categoria1,Categoria2,Vehiculo, Boleta, detalle_boleta
from .forms import CamionForm, RegistroUserForm,UserUpdateForm
from django.contrib import messages
from core.compras import Carrito

from django.db.models import Q



# Create your views here.
def es_admin(user):
    return user.is_superuser 

def home(request):
    return render(request,'home.html')

def nosotros(request):
    return render(request, 'nosotros.html')


def productos_general(request):
    camion = Vehiculo.objects.all()
    busqueda = request.GET.get("buscar")
    if busqueda: 
        camion = Vehiculo.objects.filter(
            Q(marca__icontains = busqueda) |
            Q(placa__icontains = busqueda) |
            Q(capacidad__icontains = busqueda) |
            Q(categoria1__nombre__icontains=busqueda) |
            Q(categoria2__ciudad__icontains=busqueda)
        ).distinct()
    return render(request, 'productos_general.html', {'camion':camion})

@login_required
def servicios(request):
    camion = Vehiculo.objects.all()
    busqueda = request.GET.get("buscar")
    if busqueda: 
        camion = Vehiculo.objects.filter(
            Q(marca__icontains = busqueda) |
            Q(placa__icontains = busqueda) |
            Q(capacidad__icontains = busqueda) |
            Q(categoria1__nombre__icontains=busqueda) |
            Q(categoria2__ciudad__icontains=busqueda)
        ).distinct()
    return render(request, 'servicios.html', {'camion':camion})

@login_required
def crear(request):
    if request.method == 'POST':
        camionForm = CamionForm(request.POST, request.FILES)  # Crear una instancia de CancionesForms con datos del POST
        if camionForm.is_valid():
            camionForm.save()  # Guardar el formulario si es válido (equivalente a un insert into)
            return redirect('servicios')  # Redirigir a la vista de canciones después de guardar
    else:
        camionForm = CamionForm()  # Crear una instancia vacía de CancionesForms para el formulario inicial

    return render(request, 'crear.html', {'camionForm': camionForm})  # Renderizar el template crear.html con el formulario


def detalle(request, id):
    camion = get_object_or_404(Vehiculo, placa=id)   #realiza busquedas especificas por atributo pk
    return render (request, 'detalle.html', {'camion':camion})




def modificar(request, id):
    vehiculo = Vehiculo.objects.get(placa=id)
    datos={
        'forModificar': CamionForm(instance=vehiculo),     #crea un obj de tipo formulario
        'vehiculo':  vehiculo
    }
    if request.method=='POST':
        formulario= CamionForm(request.POST, request.FILES, instance=vehiculo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El camión ha sido modificado correctamente.")
            return redirect('servicios')
        else:
            messages.error(request, "Por favor, corrija los errores en el formulario.")
    else:
        formulario = CamionForm(instance=vehiculo)
    return render(request, 'modificar.html', {'forModificar': formulario, 'vehiculo': vehiculo})


def eliminar(request, id):
    camion = get_object_or_404(Vehiculo, placa=id)
    if request.method=='POST':
        if 'eliminar' in request.POST:       #botón cuyo name es elimina en html para confirmar
            camion.delete()
            messages.success(request, 'El camión ha sido eliminado correctamente.')               #elimina el objeto despues de confirmar
            return redirect ('servicios')
        else:
            messages.info(request, 'La eliminación del camión ha sido cancelada.')
            return redirect ('detalle', placa=id)
    return render (request, 'eliminar.html', {'camion': camion})



def cerrar(request):
    logout(request)
    return redirect('home')

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=='POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('home')
        data["form"]=formulario
    return render(request, 'registration/registrar.html',data)


@login_required
def cuenta(request):
    usuario = request.user
    datos = {
        'forModificar': UserUpdateForm(instance=usuario),
        'usuario': usuario
    }
    if request.method=='POST':
        form = UserUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect ('cuenta')
    return render(request, 'cuenta.html', datos)

def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    camion = Vehiculo.objects.get(placa=id)
    carrito_compra.agregar(camion=camion)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    camion = Vehiculo.objects.get(placa=id)
    carrito_compra.eliminar(camion=camion)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    camion = Vehiculo.objects.get(placa=id)
    carrito_compra.restar(camion=camion)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    

def tienda(request):
    camion = Vehiculo.objects.all()
    datos={
        'camion':camion
    }
    return render(request, 'tienda.html', datos)


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Vehiculo.objects.get(placa = value['placa'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)


