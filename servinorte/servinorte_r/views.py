from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import usuarios
from .models import Empresa 
from .models import usuarios
from .models import marcas
from .models import Unidades_medida
from .models import Sucursales
from .models import Personal
from .models import grupos_proveedor
from .models import inventarios
from .models import lineas_articulos
from .models import sublineas_articulos
from .models import Articulos
from .models import items_inventario

from .forms import EmpresaForm, UsuarioForm, MarcaForm, UnidadForm, SucursalForm, PersonalForm, ProveedorForm, InventarioForm, LineaForm, SublineaForm, ArticuloForm, ItemForm
# Create your views here.

M=marcas;
U=usuarios;
I=inventarios;

def index(request):
    return render(request,'base.html')

def home(request):
    return render(request,"home/home.html")


def empresas(request):
    empresas=Empresa.objects.all()
    return render(request,"empresa/index.html",{'empresas':empresas})

def crear_empresa(request):
    formulario_E=EmpresaForm(request.POST or None, request.FILES or None)
    if formulario_E.is_valid():
        formulario_E.save()
        return redirect('empresa')
    return render(request,"empresa/crear.html",{'formulario_E':formulario_E})

def editar_empresa(request,id):
    empresa=Empresa.objects.get(id=id)
    formulario_E=EmpresaForm(request.POST or None, request.FILES or None,instance=empresa)
    if formulario_E.is_valid() and request.POST:
        formulario_E.save()
        return redirect('empresa')
    return render(request,"empresa/editar.html",{'formulario_E':formulario_E})

def eliminar_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    return redirect('empresa')

def usuarios(request):
    usuarios=U.objects.all()
    return render(request,"usuario/index.html",{'usuarios':usuarios})

def crear_usuario(request):
    formulario_U=UsuarioForm(request.POST or None, request.FILES or None)
    if formulario_U.is_valid():
        formulario_U.save()
        return redirect('usuario')
    return render(request,"usuario/crear.html",{'formulario_U':formulario_U})

def editar_usuario(request,id):
    usuarios=U.objects.get(id=id)
    formulario_U=UsuarioForm(request.POST or None, request.FILES or None,instance=usuarios)
    if formulario_U.is_valid() and request.POST:
        formulario_U.save()
        return redirect('usuario')
    return render(request,"usuario/editar.html",{'formulario_U':formulario_U})

def eliminar_usuario(request, id):
    usuarios = U.objects.get(id=id)
    usuarios.delete()
    return redirect('usuario')

def marcas(request):
    marcas=M.objects.all()
    return render(request,"marca/index.html",{'marcas':marcas})

def crear_marca(request):
    formulario_M=MarcaForm(request.POST or None, request.FILES or None)
    if formulario_M.is_valid():
        formulario_M.save()
        return redirect('marca')
    return render(request,"marca/crear.html",{'formulario_M':formulario_M})

def editar_marca(request,id):
    marcas=M.objects.get(id=id)
    formulario_M=MarcaForm(request.POST or None, request.FILES or None,instance=marcas)
    if formulario_M.is_valid() and request.POST:
        formulario_M.save()
        return redirect('marca')
    return render(request,"marca/editar.html",{'formulario_M':formulario_M})

def eliminar_marca(request, id):
    marcas = M.objects.get(id=id)
    marcas.delete()
    return redirect('marca')

def unidades(request):
    unidades=Unidades_medida.objects.all()
    return render(request,"unidades_medida/index.html",{'unidades':unidades})


def crear_unidad(request):
    formulario_UM=UnidadForm(request.POST or None, request.FILES or None)
    if formulario_UM.is_valid():
        formulario_UM.save()
        return redirect('unidad')
    return render(request,"unidades_medida/crear.html",{'formulario_UM':formulario_UM})

def editar_unidad(request,id):
    unidades=Unidades_medida.objects.get(id=id)
    formulario_UM=UnidadForm(request.POST or None, request.FILES or None,instance=unidades)
    if formulario_UM.is_valid() and request.POST:
        formulario_UM.save()
        return redirect('unidad')
    return render(request,"unidades_medida/editar.html",{'formulario_UM':formulario_UM})

def eliminar_unidad(request, id):
    unidades = Unidades_medida.objects.get(id=id)
    unidades.delete()
    return redirect('unidad')


def sucursales(request):
    sucursales=Sucursales.objects.all()
    return render(request,"sucursal/index.html",{'sucursales':sucursales})

def crear_sucursal(request):
    formulario_S=SucursalForm(request.POST or None, request.FILES or None)
    if formulario_S.is_valid():
        formulario_S.save()
        return redirect('sucursal')
    return render(request,"sucursal/crear.html",{'formulario_S':formulario_S})

def editar_sucursal(request,id):
    sucursales=Sucursales.objects.get(id=id)
    formulario_S=SucursalForm(request.POST or None, request.FILES or None,instance=sucursales)
    if formulario_S.is_valid() and request.POST:
        formulario_S.save()
        return redirect('sucursal')
    return render(request,"sucursal/editar.html",{'formulario_S':formulario_S})

def eliminar_sucursal(request, id):
    sucursales = Sucursales.objects.get(id=id)
    sucursales.delete()
    return redirect('sucursal')

def personal(request):
    personal=Personal.objects.all()
    return render(request,"personal/index.html",{'personal':personal})


def crear_personal(request):
    formulario_P=PersonalForm(request.POST or None, request.FILES or None)
    if formulario_P.is_valid():
        formulario_P.save()
        return redirect('personal')
    return render(request,"personal/crear.html",{'formulario_P':formulario_P})

def editar_personal(request,id):
    personal=Personal.objects.get(id=id)
    formulario_P=PersonalForm(request.POST or None, request.FILES or None,instance=personal)
    if formulario_P.is_valid() and request.POST:
        formulario_P.save()
        return redirect('personal')
    return render(request,"personal/editar.html",{'formulario_P':formulario_P})

def eliminar_personal(request, id):
    personal = Personal.objects.get(id=id)
    personal.delete()
    return redirect('personal')

def proveedores(request):
    proveedores=grupos_proveedor.objects.all()
    return render(request,"grupo_proveedor/index.html",{'proveedores':proveedores})

def crear_proveedor(request):
    formulario_G=ProveedorForm(request.POST or None, request.FILES or None)
    if formulario_G.is_valid():
        formulario_G.save()
        return redirect('proveedor')
    return render(request,"grupo_proveedor/crear.html",{'formulario_G':formulario_G})

def editar_proveedor(request,id):
    proveedores=grupos_proveedor.objects.get(id=id)
    formulario_G=ProveedorForm(request.POST or None, request.FILES or None,instance=proveedores)
    if formulario_G.is_valid() and request.POST:
        formulario_G.save()
        return redirect('proveedor')
    return render(request,"grupo_proveedor/editar.html",{'formulario_G':formulario_G})

def eliminar_proveedor(request, id):
    proveedores = grupos_proveedor.objects.get(id=id)
    proveedores.delete()
    return redirect('proveedor')

def inventarios(request):
    inventarios=I.objects.all()
    return render(request,"inventario/index.html",{'inventarios':inventarios})


def crear_inventario(request):
    formulario_I=InventarioForm(request.POST or None, request.FILES or None)
    if formulario_I.is_valid():
        formulario_I.save()
        return redirect('inventario')
    return render(request,"inventario/crear.html",{'formulario_I':formulario_I})

def editar_inventario(request,id):
    inventarios=I.objects.get(id=id)
    formulario_I=InventarioForm(request.POST or None, request.FILES or None,instance=inventarios)
    if formulario_I.is_valid() and request.POST:
        formulario_I.save()
        return redirect('inventario')
    return render(request,"inventario/editar.html",{'formulario_I':formulario_I})

def eliminar_inventario(request, id):
    inventarios = I.objects.get(id=id)
    inventarios.delete()
    return redirect('inventario')

def lineas(request):
    lineas=lineas_articulos.objects.all()
    return render(request,"linea_articulo/index.html",{'lineas':lineas})

def crear_linea(request):
    formulario_L=LineaForm(request.POST or None, request.FILES or None)
    if formulario_L.is_valid():
        formulario_L.save()
        return redirect('linea')
    return render(request,"linea_articulo/crear.html",{'formulario_L':formulario_L})

def editar_linea(request,id):
    lineas=lineas_articulos.objects.get(id=id)
    formulario_L=LineaForm(request.POST or None, request.FILES or None,instance=lineas)
    if formulario_L.is_valid() and request.POST:
        formulario_L.save()
        return redirect('linea')
    return render(request,"linea_articulo/editar.html",{'formulario_L':formulario_L})

def eliminar_linea(request, id):
    lineas = lineas_articulos.objects.get(id=id)
    lineas.delete()
    return redirect('linea')

def sublineas(request):
    sublineas=sublineas_articulos.objects.all()
    return render(request,"sublinea_articulo/index.html",{'sublineas':sublineas})

def crear_sublinea(request):
    formulario_SL=SublineaForm(request.POST or None, request.FILES or None)
    if formulario_SL.is_valid():
        formulario_SL.save()
        return redirect('sublinea')
    return render(request,"sublinea_articulo/crear.html",{'formulario_SL':formulario_SL})

def editar_sublinea(request,id):
    sublineas=sublineas_articulos.objects.get(id=id)
    formulario_SL=SublineaForm(request.POST or None, request.FILES or None,instance=sublineas)
    if formulario_SL.is_valid() and request.POST:
        formulario_SL.save()
        return redirect('sublinea')
    return render(request,"sublinea_articulo/editar.html",{'formulario_SL':formulario_SL})

def eliminar_sublinea(request, id):
    sublineas = sublineas_articulos.objects.get(id=id)
    sublineas.delete()
    return redirect('sublinea')

def articulos(request):
    articulos=Articulos.objects.all()
    return render(request,"articulo/index.html",{'articulos':articulos})

def crear_articulo(request):
    formulario_A=ArticuloForm(request.POST or None, request.FILES or None)
    if formulario_A.is_valid():
        formulario_A.save()
        return redirect('articulo')
    return render(request,"articulo/crear.html",{'formulario_A':formulario_A})

def editar_articulo(request,id):
    articulos=Articulos.objects.get(id=id)
    formulario_A=ArticuloForm(request.POST or None, request.FILES or None,instance=articulos)
    if formulario_A.is_valid() and request.POST:
        formulario_A.save()
        return redirect('articulo')
    return render(request,"articulo/editar.html",{'formulario_A':formulario_A})

def eliminar_articulo(request, id):
    articulos = Articulos.objects.get(id=id)
    articulos.delete()
    return redirect('articulo')

def items(request):
    items=items_inventario.objects.all()
    return render(request,"item_inventario/index.html",{'items':items})


def crear_item(request):
    formulario_II=ItemForm(request.POST or None, request.FILES or None)
    if formulario_II.is_valid():
        formulario_II.save()
        return redirect('item')
    return render(request,"item_inventario/crear.html",{'formulario_II':formulario_II})

def editar_item(request,id):
    items=items_inventario.objects.get(id=id)
    formulario_II=ItemForm(request.POST or None, request.FILES or None,instance=items)
    if formulario_II.is_valid() and request.POST:
        formulario_II.save()
        return redirect('item')
    return render(request,"item_inventario/editar.html",{'formulario_II':formulario_II})

def eliminar_item(request, id):
    items = items_inventario.objects.get(id=id)
    items.delete()
    return redirect('item')