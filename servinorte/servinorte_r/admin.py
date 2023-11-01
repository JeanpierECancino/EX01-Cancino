from django.contrib import admin
from .models import Empresa, usuarios, marcas, Unidades_medida, Sucursales, Personal, grupos_proveedor,inventarios,lineas_articulos,sublineas_articulos,Articulos,items_inventario
# Register your models here.
admin.site.register(Empresa)
admin.site.register(usuarios)
admin.site.register(marcas)
admin.site.register(Unidades_medida)
admin.site.register(Sucursales)
admin.site.register(Personal)
admin.site.register(grupos_proveedor)
admin.site.register(inventarios)
admin.site.register(lineas_articulos)
admin.site.register(sublineas_articulos)
admin.site.register(Articulos)
admin.site.register(items_inventario)