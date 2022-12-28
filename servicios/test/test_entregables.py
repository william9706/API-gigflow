#rest framework
from rest_framework import status
from rest_framework.test import APIClient
#models
from servicios.models import Entregables
#django imports
from django.urls import reverse
from django.test import TestCase
#serializer
from servicios.serializers import EntregableSerializer

ENTREGABLE_URL = reverse("servicios:entregable-list")

class EntregablesApiTest(TestCase):
    """ Probar API entregables. """

    def setUp(self):
        self.client = APIClient()
    
    def test_retrieve_entregables(self):
        """ Probar obtener entregable especifico. """

        Entregables.objects.create(nombre="prueba entregable 1")

        response = self.client.get(ENTREGABLE_URL)
        entregables = Entregables.objects.all().order_by('-nombre')
        serializer = EntregableSerializer(entregables, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_entregable(self):
        """ Probar que se Listen los entregables """

        self.entregable = Entregables.objects.create(
            nombre="prueba entregable 1"
        )
        response = self.client.get(ENTREGABLE_URL)
        self.assertEqual(response.data[0]['nombre'], "prueba entregable 1")

    def test_create_entregable(self):
        """ Probar crear un entregable satisfactoriamente. """

        payload = {
            'nombre':'entregable 1'
        }

        self.client.post(ENTREGABLE_URL, payload)
        exitsts = Entregables.objects.filter(
            nombre=payload['nombre']
        ).exists()
        self.assertTrue(exitsts)
    
    def test_create_invalid_entregable(self):
        """ probar si se pasa un entregable invalido(sin nada). """

        payload = {
            "nombre":""
        }
        response = self.client.post(ENTREGABLE_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    def test_delete_entregable(self):
        """
        Test para eliminar un entregable
        exitosamente.
        """
        entregable = Entregables.objects.create(nombre = 'Entregable 1')
        url = f'{ENTREGABLE_URL}{entregable.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    