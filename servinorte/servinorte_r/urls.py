from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    # ---------------------------------------------------------
    path('empresa/',views.empresas,name='empresa'),
    path('empresa/crear',views.crear_empresa,name='crear_empresa'),
    path('empresa/editar',views.editar_empresa,name='editar_empresa'),
    path('eliminar/<int:id>',views.eliminar_empresa,name='eliminar_empresa'),
    path('empresa/editar/<int:id>',views.editar_empresa,name='editar_empresa'),
    # ---------------------------------------------------------
    path('usuario/',views.usuarios,name='usuario'),
    path('usuario/crear',views.crear_usuario,name='crear_usuario'),
    path('usuario/editar',views.editar_usuario,name='editar_usuario'),
    path('usuario/<int:id>',views.eliminar_usuario,name='eliminar_usuario'),
    path('usuario/editar/<int:id>',views.editar_usuario,name='editar_usuario'),
    # ---------------------------------------------------------
    path('marca/',views.marcas,name='marca'),
    path('marca/crear',views.crear_marca,name='crear_marca'),
    path('marca/editar',views.editar_marca,name='editar_marca'),
    path('marca/<int:id>',views.eliminar_marca,name='eliminar_marca'),
    path('marca/editar/<int:id>',views.editar_marca,name='editar_marca'),
    # ---------------------------------------------------------
    path('unidad/',views.unidades,name='unidad'),
    path('unidad/crear',views.crear_unidad,name='crear_unidad'),
    path('unidad/editar',views.editar_unidad,name='editar_unidad'),
    path('unidad/<int:id>',views.eliminar_unidad,name='eliminar_unidad'),
    path('unidad/editar/<int:id>',views.editar_unidad,name='editar_unidad'),
    # ---------------------------------------------------------
    path('sucursal/',views.sucursales,name='sucursal'),
    path('sucursal/crear',views.crear_sucursal,name='crear_sucursal'),
    path('sucursal/editar',views.editar_sucursal,name='editar_sucursal'),
    path('sucursal/<int:id>',views.eliminar_sucursal,name='eliminar_sucursal'),
    path('sucursal/editar/<int:id>',views.editar_sucursal,name='editar_sucursal'),
    # ---------------------------------------------------------
    path('personal/',views.personal,name='personal'),
    path('personal/crear',views.crear_personal,name='crear_personal'),
    path('personal/editar',views.editar_personal,name='editar_personal'),
    path('personal/<int:id>',views.eliminar_personal,name='eliminar_personal'),
    path('personal/editar/<int:id>',views.editar_personal,name='editar_personal'),
    # ---------------------------------------------------------
    path('proveedor/',views.proveedores,name='proveedor'),
    path('proveedor/crear',views.crear_proveedor,name='crear_proveedor'),
    path('proveedor/editar',views.editar_proveedor,name='editar_proveedor'),
    path('proveedor/<int:id>',views.eliminar_proveedor,name='eliminar_proveedor'),
    path('proveedor/editar/<int:id>',views.editar_proveedor,name='editar_proveedor'),
    # ---------------------------------------------------------
    path('inventario/',views.inventarios,name='inventario'),
    path('inventario/crear',views.crear_inventario,name='crear_inventario'),
    path('inventario/editar',views.editar_inventario,name='editar_inventario'),
    path('inventario/<int:id>',views.eliminar_inventario,name='eliminar_inventario'),
    path('inventario/editar/<int:id>',views.editar_inventario,name='editar_inventario'),
    # ---------------------------------------------------------
    path('linea/',views.lineas,name='linea'),
    path('linea/crear',views.crear_linea,name='crear_linea'),
    path('linea/editar',views.editar_linea,name='editar_linea'),
    path('linea/<int:id>',views.eliminar_linea,name='eliminar_linea'),
    path('linea/editar/<int:id>',views.editar_linea,name='editar_linea'),
    # ---------------------------------------------------------
    path('sublinea/',views.sublineas,name='sublinea'),
    path('sublinea/crear',views.crear_sublinea,name='crear_sublinea'),
    path('sublinea/editar',views.editar_sublinea,name='editar_sublinea'),
    path('sublinea/<int:id>',views.eliminar_sublinea,name='eliminar_sublinea'),
    path('sublinea/editar/<int:id>',views.editar_sublinea,name='editar_sublinea'),
    # ---------------------------------------------------------
    path('articulo/',views.articulos,name='articulo'),
    path('articulo/crear',views.crear_articulo,name='crear_articulo'),
    path('articulo/editar',views.editar_articulo,name='editar_articulo'),
    path('articulo/<int:id>',views.eliminar_articulo,name='eliminar_articulo'),
    path('articulo/editar/<int:id>',views.editar_articulo,name='editar_articulo'),
    # ---------------------------------------------------------
    path('item/',views.items,name='item'),
    path('item/crear',views.crear_item,name='crear_item'),
    path('item/editar',views.editar_item,name='editar_item'),
    path('item/<int:id>',views.eliminar_item,name='eliminar_item'),
    path('item/editar/<int:id>',views.editar_item,name='editar_item'),
]