from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from .views import SignUpView
from . import views

urlpatterns = [
    path('registrar/',SignUpView.as_view(),name="registrar"),
    path('dashboard/', views.dashboard,name="dashboard" ),
    path('dashboard/editar-perfil',views.editarPerfil,name="editarPerfil"),
    path('password/',views.PasswordChangeView.as_view(),name="passwordChange"),
    path('admin-dashboard',views.adminDashboard,name="adminDashboard"),
    path('admin-dashboard/factura-#<int:id>',views.factura,name="factura"),
    path('admin-dashboard/agregar-producto',views.agregarProducto,name="agregarProducto"),
    path('admin-dashboard/administrar-usuario/<int:id>',views.administrarUsuarios,name="administrarUsuarios")    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)