from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


from sp.models import OrdenPago
from account.models import CustomUser
from .models import ProductoFijo, CartProduct

from .forms import *


# Create your views here.

def marketplace(request):
    items = ProductoFijo.objects.all()

    if request.method == 'POST':
        form = cantidad(request.POST)

        # Traer Usuario
        user = request.user.username
        propietario = CustomUser.objects.get(username=user)

        if form.is_valid():

            # Asignando la data
            data = form.cleaned_data

            q = data['cantidad']
            idKey = data['id']

            # Obteniendo el nombre del producto con una query
            item = ProductoFijo.objects.get(pk=idKey)


            item.cantidadDisponible = item.cantidadDisponible - q
            item.cantidadVendida=item.cantidadVendida + q
            item.save()

            # Obteniendo el color desde el formulario
            colores = data['colores']
            # cantidad

            # si no existe, creamos una nueva cantidad
            quantity = int(q)

            # Precio por unidad desde la query
            precioUnitario = int(item.precio)

            # precioTotal
            precioTotal = precioUnitario * q

            # Preparamos el insert
            addToCart = CartProduct(
                propietario=propietario,
                nombre=item,
                cantidad=quantity,
                color=colores,
                precioUnitario=precioUnitario,
                total=precioTotal,
                ordenPago=0)

            # Salvamos el producto en la tabla de instancias
            addToCart.save()

            

           

            return redirect('marketplace')
    else:
        form = cantidad()

    

    context = {'items': items, 'form': form, 'verify':0}
    return render(request, 'marketplace/market.html', context)

def vistaPrueba(request):

    context = {}
    return render(request, 'marketplace/view.html', context)

def carrito(request):

    if request.user.username:

        user = request.user.username
        propietario = CustomUser.objects.get(username=user)
        userId = propietario.id

        cart = CartProduct.objects.filter(
            propietario=userId).filter(status="En proceso")

        suma = 0
        for item in cart:
            suma = suma + int(item.total)

        iva = suma * 0.16

        totalFinal = iva + suma

        context = {
            'cart': cart,
            'userId': userId,
            'suma': suma,
            'totalFinal': totalFinal,
            'iva': iva
        }

        return render(request, 'marketplace/carrito.html', context)
    else:
        context = {}
        return redirect('login')

def editarItem(request, id):

    if request.user.is_authenticated:

        objeto = CartProduct.objects.filter(pk=id).first()
        name = objeto.nombre
        precio = objeto.precioUnitario

        if request.method == 'POST':
            form = EditarItemCarrito(request.POST, instance=objeto)

            if form.is_valid():
                data = form.cleaned_data
                quantity = data['cantidad']

                newTotal = int(precio) * int(quantity)

                objeto.total = newTotal

                objeto.save()
                form.save()
                return redirect('carrito')
        else:
            form = EditarItemCarrito(instance=objeto)

        context = {
            'form': form,
            'name': name,
            'pageName': 'Editar Articulo',
            'title': 'Editar Articulo del Carrito: '+ str(name),
            'btnName': 'Enviar'
        }

        return render(request, 'sp/form.html', context)

    else:
        return redirect('home')

def eliminarItem(request, id):

    cart = CartProduct.objects.filter(id=id)
    cart.delete()

    return redirect('carrito')

def pagarItem(request):

    propietario = CustomUser.objects.get(username=request.user.username)
    userId = propietario.id
    cart = CartProduct.objects.filter(
        propietario=userId).filter(status="En proceso")

    facturaQuery = OrdenPago.objects.get(id=1)
    factura = facturaQuery.numeroOrden

    for item in cart:
        item.status = "Pagado"
        item.ordenPago = factura
        item.save()

    # Cambiar el orden de la factura (por ahora)
    factura = OrdenPago.objects.get(id=1)

    valor = factura.numeroOrden
    factura.numeroOrden = valor + 1
    factura.save()

    return redirect('carrito')


# VISTA DE ADMIN

def editarProductoMarket(request, id):


    if request.user.is_authenticated:

        objeto = ProductoFijo.objects.filter(pk=id).first()
        

        if request.method == 'POST':
            form = HandleStockItem(request.POST, instance=objeto)

            if form.is_valid():
            
                form.save()
                return redirect('marketplace')
        else:
            form = HandleStockItem(instance=objeto)


    context={
        'form':form,
        'pageName':'Cambiar Producto',
        'title': 'Actualizacion de producto',
        'btnName':'Actualizar'
    }

    return render(request,'sp/form.html',context)

