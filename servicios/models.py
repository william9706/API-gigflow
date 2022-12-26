from django.db import models




class TiposServicios(models.Model):
    """ Modelo para la tabla tipos de servicios. """

    nombre = models.CharField(
        max_length=55,
        null=True,
        blank=True,
        verbose_name="Nombre"
    )

    class Meta:
        verbose_name = "Tipo de Servicio"
        verbose_name_plural = "Tipos de Servicios"
    
    def __str__(self):
        return self.nombre


class Entregables(models.Model):
    """ Modelo para tabla para entregables """
    #TODO: se agrega una 3 tabla para entregables.

    nombre = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="Nombre del entregable"
    )

    class Meta:
        verbose_name = "Entregable"
        verbose_name_plural = "Entregables"
    
    def __str__(self):
        return self.nombre


class Paquetes(models.Model):
    """ Modelo para tabla paquete. """

    descripcion = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        verbose_name="Descripcion"
    )

    precio = models.IntegerField(
        max_length=100,
        null=True,
        blank=False,
        verbose_name="Precio"
    )

    entregables = models.ManyToManyField(
        Entregables,
        max_length=200,
        blank=True,
        verbose_name="Entregables"
    )

    servicios = models.ForeignKey(
        TiposServicios,
        null=True,
        blank=True,
        verbose_name="Servicios",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Paquete"
        verbose_name_plural = "Paquetes"

    def __str__(self):
        return self.descripcion
