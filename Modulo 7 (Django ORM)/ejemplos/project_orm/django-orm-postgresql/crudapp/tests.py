from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

from .models import Empleado

# Pruebas de páginas estáticas

class InicioTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/crudapp/inicio/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(response, 'inicio.html')

    def test_template_content(self):
        response = self.client.get(reverse('inicio'))
        self.assertContains(response, '<h1>Página de inicio</h1>')
        self.assertNotContains(response, 'No es la Página')

# Pruebas de web app

class EmpleadoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.empleado = Empleado.objects.create(emp_id='123', emp_nombre='Juan', emp_correo='juan@test.com', emp_designacion='Desarrollo Web')
    
    def test_model_content(self):
        self.assertEqual(self.empleado.emp_id,'123')
        self.assertEqual(self.empleado.emp_nombre,'Juan')
        self.assertEqual(self.empleado.emp_correo,'juan@test.com')
        self.assertEqual(self.empleado.emp_designacion,'Desarrollo Web')

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/crudapp/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('mostrar-emp'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mostrar.html')
        self.assertContains(response, 'Información de Empleados')