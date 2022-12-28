#rest framework
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
#models
from servicios.models import Paquetes, Entregables
#django imports
from django.urls import reverse
from django.test import TestCase
#serializer
from servicios.serializers import PaquetesSerializer

PAQUETES_URL = reverse("servicios:paquete-list")

    

class PaquetesApiTest(APITestCase):
    """ Probar API paquetes. """

    def setUp(self):
        self.client = APIClient()
        self.entregable = Entregables.objects.create(
            nombre="prueba entregable 1"
        )

    def create_entregable(self):
        data = {'nombre': 'prueba entregable 1'}
        return Entregables.objects.create(**data)


    def create_paquete(self):
        data = {
            "descripcion":"prueba paquete 1",
            "precio":2000
        }
        paquete = Paquetes.objects.create(**data)
        entregable = self.create_entregable()
        paquete.entregables.add(entregable)
        return paquete

##################################### Test ##########################################
    def test_retrieve_paquete(self):
        """ Probar obtener paquete específico. """

        self.paquete = Paquetes.objects.create(
            descripcion="prueba paquete 1", 
            precio=2000,
        )
        self.paquete.entregables.add(self.entregable)

        response = self.client.get(PAQUETES_URL)
        paquetes = Paquetes.objects.all().order_by('-descripcion')
        serializer = PaquetesSerializer(paquetes, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_paquetes(self):
        """ Probar que se Listen los paquetes. """

        self.paquete = Paquetes.objects.create(
            descripcion="prueba paquete 1",
            precio= 3000
        )
        self.paquete.entregables.add(self.entregable)
        response = self.client.get(PAQUETES_URL)
        self.assertEqual(response.data[0]['descripcion'], "prueba paquete 1")
    

    def test_create_paquete(self):
        """ Probar crear un paquete satisfactoriamente. """

        self.paquete = self.create_paquete()

        self.assertEqual(Paquetes.objects.count(), 1)
        self.assertEqual(self.paquete.descripcion, 'prueba paquete 1')


    def test_create_invalid_paquete(self):
        """ probar si se pasa un paquete invalido(sin nada). """

        payload = {
            "descripcion":"",
            "precio":"",
            "entregables":[]
        }
        response = self.client.post(PAQUETES_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    def test_delete_entregable(self):
        """
        Test para eliminar un paquete
        exitosamente.
        """
        paquete = Paquetes.objects.create(
            descripcion = 'Prueba paquete 1', 
            precio=3000
        )
        paquete.entregables.add(self.entregable)
        
        response = self.client.delete(
            f'{PAQUETES_URL}{paquete.id}/'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    