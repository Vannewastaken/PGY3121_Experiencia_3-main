from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name="home"),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('crear/',views.crear, name="crear"),
    path('detalle/<id>/', views.detalle, name="detalle"),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminar_camion/<id>/', views.eliminar, name="eliminar"),
    path('logout/', views.cerrar, name="cerrar"),
    path('registrar/', views.registrar, name="registrar"),
    path('forget/', views.forgetpassword, name="forget"),
    
    path('tienda/',views.tienda, name="tienda"),
    path('agregar/<id>', views.agregar_producto, name="agregar"),
    path('eliminar/<id>', views.eliminar_producto, name="eliminar_producto"),
    path('restar/<id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),
    path('generarBoleta/', views.generarBoleta,name="generarBoleta"),

]