#rest framework
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
#models
from servicios.models import Paquetes, Entregables, Servicios
#django imports
from django.urls import reverse
from django.test import TestCase
#serializer
from servicios.serializers import ServicioSerializer

SERVICIOS_URL = reverse("servicios:servicio-list")

    

class ServicviosApiTest(APITestCase):
    """ Probar API servicios. """

    def setUp(self):
        self.client = APIClient()
        self.entregable = Entregables.objects.create(
            nombre="prueba entregable 1"
        )
        self.paquete = Paquetes.objects.create(
            descripcion="paquete prueba 1",
            precio=3000
        )
        self.paquete.entregables.add(self.entregable)
    
    def create_servicio(self):
        data = {
            "nombre":"prueba servicio 1",
        }
        servicio = Servicios.objects.create(**data)
        servicio.paquetes.add(self.paquete)
        return servicio

##################################### Test ##########################################
    def test_retrieve_servicio(self):
        """ Probar obtener servicio específico. """

        self.servicio = Servicios.objects.create(
            nombre="prueba servicio 1", 
        )
        self.servicio.paquetes.add(self.paquete)

        response = self.client.get(SERVICIOS_URL)
        servicios = Servicios.objects.all().order_by('-nombre')
        serializer = ServicioSerializer(servicios, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_servicio(self):
        """ Probar que se Listen los servicios. """

        self.servicio = Servicios.objects.create(
            nombre="prueba servicio 1",
        )
        self.servicio.paquetes.add(self.paquete)
        response = self.client.get(SERVICIOS_URL)
        self.assertEqual(response.data[0]['nombre'], "prueba servicio 1")
    

    def test_create_servicio(self):
        """ Probar crear un servicio satisfactoriamente. """

        self.servicio = self.create_servicio()

        self.assertEqual(Servicios.objects.count(), 1)
        self.assertEqual(self.servicio.nombre, 'prueba servicio 1')


    def test_create_invalid_servicio(self):
        """ probar si se pasa un servicio invalido(sin nada). """

        payload = {
            "descripcion":"",
            "paquetes":[]
        }
        response = self.client.post(SERVICIOS_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    def test_delete_servicio(self):
        """
        Test para eliminar un servicio
        exitosamente.
        """
        servicio = Servicios.objects.create(
            nombre = 'Prueba servicio 1', 
        )
        servicio.paquetes.add(self.paquete)
        
        response = self.client.delete(
            f'{SERVICIOS_URL}{servicio.id}/'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    