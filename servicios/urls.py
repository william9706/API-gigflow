from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from servicios import views


router = routers.DefaultRouter()
router.register('servicios', views.ServiciosViewSet)
router.register('entregables', views.EntregablesViewSet)
router.register('paquetes', views.PaquetesViewSet)


app_name = 'tipos-servicios'

urlpatterns = [
    path('', include(router.urls))
]
