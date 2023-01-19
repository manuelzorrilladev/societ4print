from django import forms
from .models import CartProduct,ProductoFijo
from .choices import SELECCION_COLORES




class cantidad(forms.Form):
    id=forms.IntegerField(widget=forms.HiddenInput())
    cantidad = forms.IntegerField()
    colores=forms.ChoiceField(choices=SELECCION_COLORES,widget=forms.RadioSelect)


class HandleStockItem(forms.ModelForm):
    

    class Meta:
        model = ProductoFijo
        fields = [
            'nombreProducto',
            'precio',
            'precioCompra',
            'cantidadDisponible',
            'thumb', 
        ]
        labels={
            'nombreProducto': 'Nombre',
            'precio':'Precio de Venta',
            'cantidadDisponible':'Cantidad Comprada',
            'precioCompra': 'Precio de Compra',
            'thumb':'Imagen del producto', 
        }


class EditarItemCarrito(forms.ModelForm):

    class Meta:
        model = CartProduct
        fields= [
            'cantidad',
            'color'
        ]

