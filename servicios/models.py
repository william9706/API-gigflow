from django.db import models




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
        blank=True,
        verbose_name="Entregables"
    )


    class Meta:
        verbose_name = "Paquete"
        verbose_name_plural = "Paquetes"



class Servicios(models.Model):
    """ Modelo para la tabla tipos de servicios. """

    nombre = models.CharField(
        max_length=55,
        null=False,
        blank=True,
        verbose_name="Nombre"
    )

    paquetes = models.ManyToManyField(
        Paquetes,
        blank=True,
        verbose_name="Paquetes"

    )

    class Meta:
        verbose_name = "Tipo de Servicio"
        verbose_name_plural = "Tipos de Servicios"
    