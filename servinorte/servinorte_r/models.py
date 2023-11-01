from django.db import models

# Create your models here.
class Empresa(models.Model):
    nro_documento = models.CharField(
        max_length=11, help_text="El nro.documento de la empresa. "
    )
    razon_social = models.CharField(
        max_length=150, help_text="La razón social de la empresa. "
    )
    direccion = models.CharField(
        max_length=150, help_text="La direccion de la empresa. "
    )

    def __str__(self):
        return self.razon_social
    def delete(self,using=None, keep_parents=False):
        super().delete()


class usuarios(models.Model):
    full_name = models.CharField(max_length=100, help_text="El nombre completo del usuario. ")
    email = models.EmailField(help_text="El correo electronico del usuario. ")
    password = models.CharField(max_length=100, help_text="La contraseña del usuario. ")

    def __str__(self):
        return self.full_name


class marcas(models.Model):
    codigo_marca = models.CharField(max_length=14, help_text="El codigo de la marca. ")
    marca_nombre = models.CharField(max_length=150, help_text="El nombre de la marca. ")

    def __str__(self):
        return self.marca_nombre

class Unidades_medida(models.Model):
    unidad_medida_id = models.CharField(
        max_length=10, help_text="El id de la unidad de medida. "
    )
    unidad_nombre = models.CharField(
        max_length=150, help_text="El nombre de la unidad de medida. "
    )

    def __str__(self):
        return self.unidad_nombre 


class Sucursales(models.Model):
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre_comercial = models.CharField(
        max_length=150, help_text="El nombre comercial de la empresa. "
    )
    direccion = models.CharField(
        max_length=150, help_text="La direccion de la empresa. "
    )

    def __str__(self):
        return self.nombre_comercial


class Personal(models.Model):
    class PersonalRole(models.TextChoices):
        DNI = "1"
        CARNET = "0"

    nombre_personal = models.CharField(
        max_length=100, help_text="El nombre del trabajador. "
    )
    direccion_personal = models.CharField(
        max_length=150, help_text="La direccion del trabajador. "
    )
    tipo_documento = models.CharField(
        verbose_name="El tipo de documento del trabajador. ",
        choices=PersonalRole.choices,
        max_length=1,
    )
    nro_documento = models.CharField(
        max_length=11, help_text="El nro.documento del trabajador. "
    )
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_personal


class grupos_proveedor(models.Model):
    class ProveedorRole(models.TextChoices):
        ACTIVO = "1"
        INACTIVO = "0"

    codigo_grupo = models.CharField(max_length=15, help_text="El codigo del grupo. ")
    grupo_descripcion = models.CharField(
        max_length=100, help_text="La descripcion del grupo. "
    )

    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    activo = models.CharField(
        verbose_name="La validacion de situacion es. ",
        choices=ProveedorRole.choices,
        max_length=1,
    )

    def __str__(self):
        return self.grupo_descripcion


class inventarios(models.Model):
    class InventarioRole(models.TextChoices):
        CLOSED = "2"
        PROGRESS = "1"
        PENDING = "0"

    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    Sucursales = models.ForeignKey(Sucursales, on_delete=models.CASCADE)

    fecha_inventario = models.DateTimeField(
        auto_now_add=True, help_text="La fecha de inventario. "
    )

    nro_inventario = models.FloatField(help_text=("El nro.inventario. "))

    Personal = models.ForeignKey(Personal, on_delete=models.CASCADE)

    hora_inicio = models.DateTimeField(
        null=True, help_text="Hora de inicio de inventario. "
    )

    hora_fin = models.DateTimeField(
        null=True, help_text="Hora de final de inventario. "
    )

    estado = models.CharField(
        verbose_name="La validacion de situacion es. ",
        choices=InventarioRole.choices,
        max_length=1,
    )

    creado_por = models.CharField(max_length=15, help_text=("Fue creado por. "))

    fecha_creacion = models.DateTimeField(
        null=True, help_text=("La fecha de creacion de inventario. ")
    )

    def __str__(self):
        return self.estado


class lineas_articulos(models.Model):
    class LineaArticuloRole(models.TextChoices):
        ACTIVO = "1"
        INACTIVO = "0"

    codigo_linea = models.CharField(
        max_length=15, help_text="El codigo de la linea de articulos. "
    )
    linea_descripcion = models.CharField(
        max_length=100, help_text="La descripcion de la linea de articulos. "
    )
    grupos_proveedor = models.ForeignKey(grupos_proveedor, on_delete=models.CASCADE)

    activo = models.CharField(
        verbose_name="La validacion de situacion es. ",
        choices=LineaArticuloRole.choices,
        max_length=1,
    )

    def __str__(self):
        return self.linea_descripcion


class sublineas_articulos(models.Model):
    class SubLineaArticuloRole(models.TextChoices):
        ACTIVO = "1"
        INACTIVO = "0"

    codigo_sublinea = models.CharField(
        max_length=15, help_text="El codigo de la sublinea. "
    )
    sublinea_descripcion = models.CharField(
        max_length=100, help_text="La descripcion de la sublinea. "
    )
    lineas_articulos = models.ForeignKey(lineas_articulos, on_delete=models.CASCADE)

    estado = models.CharField(
        verbose_name="La validacion de estado es. ",
        choices=SubLineaArticuloRole.choices,
        max_length=1,
    )

    def __str__(self):
        return self.sublinea_descripcion


class Articulos(models.Model):
    codigo_sku = models.CharField(max_length=25, help_text="El codigo de articulo. ")

    descripcion = models.CharField(
        max_length=150, help_text="La descripcion del articulo. "
    )

    Unidades_medida = models.ForeignKey(Unidades_medida, on_delete=models.CASCADE)

    grupos_proveedor = models.ForeignKey(grupos_proveedor, on_delete=models.CASCADE)

    lineas_articulos = models.ForeignKey(lineas_articulos, on_delete=models.CASCADE)

    sublineas_articulos = models.ForeignKey(
        sublineas_articulos, on_delete=models.CASCADE
    )

    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    factor_compra = models.IntegerField(help_text="El factor compra. ")

    factor_reparto = models.IntegerField(help_text="El factor venta. ")

    marcas = models.ForeignKey(marcas, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class items_inventario(models.Model):
    inventarios = models.ForeignKey(inventarios, on_delete=models.CASCADE)

    nro_item = models.IntegerField(help_text="El numero de item. ")
    Articulos = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    stock_fisico = models.FloatField(max_length=12, help_text=("El stock fisico. "))
    devoluciones_pendientes = models.FloatField(max_length=12, help_text=("Las devoluciones pendientes. "))
    total_unidades_stock = models.FloatField(max_length=12, help_text=("El total de unidades en stock. "))
    precio_costo = models.FloatField(max_length=12, help_text=("El precio. "))
    total_item = models.FloatField(max_length=12, help_text=("El total. "))

    def __str__(self):
        return str(self.nro_item)