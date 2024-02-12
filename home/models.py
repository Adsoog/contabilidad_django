from django.db import models

# Create your models here.
# models.py


class Inven(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)


class OrdenDeVenta(models.Model):
    codigo_sap = models.CharField(max_length=50, null=True)
    nombre_proyecto = models.CharField(max_length=100, null=True)
    direccion_proyecto = models.CharField(max_length=255, null=True)
    fecha = models.DateField(null=True)
    observacion = models.TextField(null=True)

    def __str__(self):
        return f"OrdenDeVenta {self.codigo_sap}"


class ItemOfertaDeVenta(models.Model):
    orden_venta = models.ForeignKey(OrdenDeVenta, on_delete=models.CASCADE)
    numero_oferta = models.IntegerField()  # Nuevo atributo para identificar la oferta
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"ItemOfertaDeVenta {self.numero_oferta} - {self.nombre} - {self.orden_venta}"
