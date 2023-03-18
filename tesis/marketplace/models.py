from django.db import models


from account.models import CustomUser

# Create your models here.
class ProductoFijo(models.Model):
    nombreProducto = models.CharField(max_length=15, null=False, default='producto')
    precio = models.PositiveIntegerField()
    thumb = models.ImageField(upload_to='pimg/')
    cantidadDisponible = models.PositiveIntegerField(default=1)
    cantidadVendida = models.PositiveIntegerField(default=0)
    precioCompra = models.PositiveIntegerField(default=0)
    

    
    
    def __str__(self):
        return self.nombreProducto
    


    

class CartProduct(models.Model):
    propietario=models.ForeignKey(to=CustomUser,related_name='usuario', on_delete=models.CASCADE,default=0)
    nombre=models.ForeignKey(to=ProductoFijo, on_delete=models.CASCADE,default=1,unique=False,related_name='name')
    cantidad = models.PositiveIntegerField()
    color=models.CharField(max_length=25, default='Negro')
    tamañoDiseño=models.CharField(max_length=10, default='null')
    precioUnitario=models.PositiveIntegerField()
    total= models.PositiveIntegerField()
    status=models.CharField(max_length=20,default='En proceso')
    ordenPago=models.PositiveIntegerField(default=0)

    

    def __int__(self):
        return int(self.total)

    def __str__(self):
        return str(self.nombre)


    