from django.contrib import admin
from .models import Proveedor, Medicamento, Cliente, Venta, DetalleVenta

admin.site.register(Proveedor)
admin.site.register(Medicamento)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)


# Register your models here.
