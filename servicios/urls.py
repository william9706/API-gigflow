#django imports
from django.urls import path, include
#rest frameworks imports
from rest_framework import routers
#views
from servicios import views

app_name = 'servicios'

router = routers.DefaultRouter()
router.register('servicios', views.ServiciosViewSet, basename='servicio')
router.register('entregables', views.EntregablesViewSet, basename='entregable')
router.register('paquetes', views.PaquetesViewSet, basename="paquete")


urlpatterns = [
    path('', include(router.urls))
]
