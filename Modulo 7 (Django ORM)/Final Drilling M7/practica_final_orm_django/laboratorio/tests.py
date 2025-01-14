from django.test import TestCase
from django.urls import reverse

from .models import Laboratorio

class LaboratorioTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio Tercermundista',ciudad='Ciudad Tercermundista',pais='Pais Tercermundista')

    def test_model_content_laboratorio(self): # Prueba de coincidencia de datos simulados
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio Tercermundista')
        self.assertEqual(self.laboratorio.ciudad, 'Ciudad Tercermundista')
        self.assertEqual(self.laboratorio.pais, 'Pais Tercermundista')

    def test_url_exists_at_correct_location_laboratorio(self): # Prueba que verifica ruta raíz de la app
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_homepage_laboratorio(self): # Verificaciones de página principal
        response = self.client.get(reverse('insertar-lab'))
        self.assertEqual(response.status_code, 200) # Funciona
        self.assertTemplateUsed(response, 'laboratorio/insertar.html') # Usa el template esperado
        self.assertContains(response, '<h2>Ingresar los Datos del Laboratorio</h2>') # Posee datos esperados