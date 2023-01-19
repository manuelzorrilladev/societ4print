from django.db import models



# Create your models here.

class OrdenPago(models.Model):
    numeroOrden = models.PositiveIntegerField()

    def __int__(self):
        return self.numeroOrden



















    
    
