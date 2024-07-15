from django.contrib import admin
from .models import Categoria1, Categoria2, Vehiculo,Boleta, detalle_boleta

admin.site.register(Categoria1)
admin.site.register(Categoria2)
admin.site.register(Vehiculo)
admin.site.register(Boleta)
admin.site.register(detalle_boleta)