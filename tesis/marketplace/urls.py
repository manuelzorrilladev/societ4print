from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('marketplace/', views.marketplace ,name="marketplace"),
    path('marketplace/vistaprueba',views.vistaPrueba,name="vistaPrueba"),
    path('marketplace/carrito/',views.carrito,name='carrito'),
    path('marketplace/carrito/<int:id>', views.eliminarItem,name='eliminarItem'),
    path('marketplace/carrito/editar/<int:id>', views.editarItem,name='editarItem'),
    path('marketplace/pagar',views.pagarItem, name='pagar'),
    path('marketplace/editar/<int:id>',views.editarProductoMarket, name='editarProductoMarket'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

