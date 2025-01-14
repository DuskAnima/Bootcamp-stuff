from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

from .models import Fabrica, Producto

class StaticTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self): # Verifica si la url (absoluta) es la correcta.
        response = self.client.get('/productos/agregar/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): # Verifica si el nombre en la url es correcta.
        response = self.client.get(reverse('agregar'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self): # Verifica si la url está asignada al template correcto.
        response = self.client.get(reverse('agregar'))
        self.assertTemplateUsed(response, 'productos_del_proyecto/agregar.html')

    def test_template_content(self): # Verifica si la url posee el contenido esperado.
        response = self.client.get(reverse('agregar'))
        self.assertContains(response, '<h1>Agregar Producto</h1>')
        self.assertNotContains(response, 'No es la página')

class FabricaTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fabrica = Fabrica.objects.create(nombre='fabrica Pulenta', pais='Pais tercermundista')

    def test_model_content_fabrica(self):
        self.assertEqual(self.fabrica.nombre,'fabrica Pulenta')
        self.assertEqual(self.fabrica.pais,'Pais tercermundista')

class ProductoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.fabrica = Fabrica.objects.create(nombre='fabrica Pulenta', pais='Pais tercermundista')
        cls.producto = Producto.objects.create(nombre='Producto Pulento', precio=150, descripcion='hice giso', fabrica=cls.fabrica, f_vencimiento='2025-12-12')

    def test_model_content_producto(self):
        self.assertEqual(self.producto.nombre, 'Producto Pulento')
        self.assertEqual(self.producto.precio, 150)
        self.assertEqual(self.producto.descripcion, 'hice giso')
        self.assertEqual(self.producto.fabrica, self.fabrica)
        self.assertEqual(self.producto.f_vencimiento, '2025-12-12')

        #Bases de datos culiás.