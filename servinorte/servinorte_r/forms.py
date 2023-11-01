from django import forms
from .models import Empresa, usuarios, marcas, Unidades_medida, Sucursales, Personal, grupos_proveedor,inventarios,lineas_articulos,sublineas_articulos,Articulos,items_inventario

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = '__all__'

class MarcaForm(forms.ModelForm):
    class Meta:
        model = marcas
        fields = '__all__'

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidades_medida
        fields = '__all__'

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        fields = '__all__'

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = grupos_proveedor
        fields = '__all__'

class InventarioForm(forms.ModelForm):
    class Meta:
        model = inventarios
        fields = '__all__'

class LineaForm(forms.ModelForm):
    class Meta:
        model = lineas_articulos
        fields = '__all__'

class SublineaForm(forms.ModelForm):
    class Meta:
        model = sublineas_articulos
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model = items_inventario
        fields = '__all__'
