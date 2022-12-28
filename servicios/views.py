from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from servicios import serializers, models


class ServiciosViewSet(viewsets.ModelViewSet):
    """ Endpoint para Servicios """
    queryset = models.Servicios.objects.all()
    serializer_class = serializers.ServicioSerializer
    search_fields = ['nombre']


class EntregablesViewSet(viewsets.ModelViewSet):
    """ Endpoint para entregables. """
    serializer_class = serializers.EntregableSerializer
    queryset = models.Entregables.objects.all()


class PaquetesViewSet(viewsets.ModelViewSet):
    """ Endpoint para entregables. """
    serializer_class = serializers.PaquetesSerializer
    queryset = models.Paquetes.objects.all()
    search_fields = ['nombre']

