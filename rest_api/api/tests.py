from django.test import TestCase, Client
from http import HTTPStatus

from .models import EducationalModules


class EducationalURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.educational = EducationalModules.objects.create(
            name='Test_name',
            description='Test_description',
        )

    def setUp(self):
        self.guest_client = Client()

    def test_check_status_200(self):
        """Проверяем GET запрос к ендпоинту"""
        response = self.guest_client.get('/api/educational/', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_check_specific_content(self):
        """Проверка GET запроса к конкретному эндпоинту"""
        response = self.guest_client.get('/api/educational/1/', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_unexisting_page(self):
        """Неизвестная страница не найдена"""
        response = self.guest_client.get('/unexisting_page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_check_status_201(self):
        """Проверка POST запроса к эндпоинту"""
        educational = EducationalModules.objects.count()
        educational_form = {
            'name': 'Test_name',
            'description': 'Test_description',
        }
        response = self.guest_client.post(path='/api/educational/', data=educational_form, follow=True)
        self.assertEqual(EducationalModules.objects.count(), educational + 1)
        self.assertEqual(self.educational.description, educational_form['description'])
        self.assertEqual(self.educational.name, educational_form['name'])

    def test_put_or_patch(self):
        """Проверка запроса PUT или PATCH к эндпоинту"""
        educational_count = EducationalModules.objects.count()
        educational_form = {
            'name': "Изменение имени",
            'description': 'Изменение описания',
        }
        response = self.guest_client.post(path='/api/educational/1/', data=educational_form, follow=True)
        self.assertEqual(EducationalModules.objects.count(), educational_count)
        self.assertEqual(educational_form['name'], 'Изменение имени')
        self.assertEqual(educational_form['description'], 'Изменение описания')
