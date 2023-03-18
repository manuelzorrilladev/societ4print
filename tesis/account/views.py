from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from sp.models import OrdenPago
from marketplace.models import CartProduct,ProductoFijo
from marketplace.forms import HandleStockItem

from .forms import CustomUserCreationForm,CustomUserChangeForm,AddPermission
from .models import CustomUser

# Create your views here.
# Vistas basadas en clases
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registro.html"
    

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='sp/form.html'
    success_url = reverse_lazy("dashboard")
    extra_context = {
        'pageName':'Cambiar Contraseña',
        'title': 'Cambiar Contraseña',
        'btnName':'Cambiar'

    }


#Vistas basadas en funciones
def dashboard(request):
    
    if request.user.is_staff:
        return redirect('adminDashboard')
    else:

        user = request.user.username


        
        if user:
            propietario = CustomUser.objects.get(username=user)
            query = CartProduct.objects.filter(propietario=propietario).filter(status="En proceso")
            
            if query.exists():
                context= {'query':query}
            else:
                context={}
            
            return render(request,'account/dashboard.html',context)
        
        else:
            
            return render(request,'account/dashboard.html')

def editarPerfil(request):

    usuario = request.user.username
    query = CustomUser.objects.get(username=usuario)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=query)

        if form.is_valid():
            form.save()

            if request.user.is_staff:
                return redirect('adminDashboard')
            else:
                return redirect('dashboard')
    else:
        form = CustomUserChangeForm(instance=query)


    context = {
        'form':form,
        'pageName':'Editar Perfil',
        'title': 'Editar Perfil',
        'btnName':'Guardar'
    }
    return render(request,'sp/form.html',context)


# VISTAS DEL ADMIN

def adminDashboard(request):

    if not request.user.is_staff:
        return redirect('dashboard')
    else:

        productos = CartProduct.objects.filter(status="Pagado")
        factura = OrdenPago.objects.get(id=1)
        valor = int(factura.numeroOrden)

        inventario = ProductoFijo.objects.all()


        users = CustomUser.objects.exclude(username='')
        
        
        

        

        
        context = {
            'productos':productos,
            'valor':valor,
            'range':range(1,valor),
            'users':users,
            'inventario':inventario
            }
        return render(request,'account/adminDashboard.html',context )
        
def administrarUsuarios(request,id):
    if request.user.is_superuser:
        
        usuario = CustomUser.objects.get(id=id)
        userName=usuario.username

        if usuario.is_staff:
            staff=1
        else:
            staff=0

        if request.method == 'POST':
            form = AddPermission(request.POST,instance=usuario)
            if form.is_valid():
                form.save()
                return redirect('adminDashboard')
        else:
            form=AddPermission(instance=usuario)        
        
        
        context = {
            'usuario':usuario,
            'userName':userName,
            'staff':staff,
            'form':form
            }





        return render(request,'account/administracion.html',context)








    else:
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('adminDashboard')
            else:
                return redirect('Dashboard')
            
def factura(request,id):

    cart = CartProduct.objects.filter(ordenPago=id).filter(status="Pagado")

    userQuery = CartProduct.objects.filter(ordenPago=id).filter(status="Pagado").first()
    propietario = userQuery.propietario
    user = CustomUser.objects.get(username=propietario)
    

    suma = 0
    for item in cart:
        suma = suma + int(item.total)

    iva = suma * 0.16

    totalFinal = iva + suma


    context= {
        'cart':cart,
        'suma':suma, 
        'totalFinal':totalFinal,
        'iva':iva,
        'id':id,
        'verify':True,
        'user':user
        }
    return render(request,'account/factura.html',context)

def agregarProducto(request):
    if request.user.is_staff:
        
        if request.method == 'POST':
            form = HandleStockItem(request.POST,request.FILES)

            if form.is_valid():
            
                form.save()

                return redirect('adminDashboard')

        else:
            form = HandleStockItem()


        context = {
            'form': form,
            'pageName':'Agregar Producto',
            'title': 'Nuevo producto',
            'btnName':'Agregar'
            
            }

        return render(request,'sp/form.html',context)


