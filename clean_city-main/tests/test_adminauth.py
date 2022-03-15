from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class SignupTestCase(APITestCase):
    def test_signup(self):
        data = {
            "first_name": "test",
            "last_name": "test-chi",
            "email": "test@cleancityllc.com",
            "password": 'test12345678',
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get('email'), "test@cleancityllc.com")
