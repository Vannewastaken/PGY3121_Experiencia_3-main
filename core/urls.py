from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns= [
    path('', views.home, name="home"),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('productos_general/', views.productos_general, name='productos_general'),
    path('crear/',views.crear, name="crear"),
    path('detalle/<id>/', views.detalle, name="detalle"),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminar_camion/<id>/', views.eliminar, name="eliminar"),
    path('logout/', views.cerrar, name="cerrar"),
    path('registrar/', views.registrar, name="registrar"),
    path('cuenta/', views.cuenta, name="cuenta"),

    
    path('tienda/',views.tienda, name="tienda"),
    path('agregar/<id>', views.agregar_producto, name="agregar"),
    path('eliminar/<id>', views.eliminar_producto, name="eliminar_producto"),
    path('restar/<id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),
    path('generarBoleta/', views.generarBoleta,name="generarBoleta"),

    path('boleta/', views.boleta, name="boleta"),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password-reset-form.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password-reset-done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password-reset-confirm.html"), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password-reset-complete.html'), name='password_reset_complete'),
]