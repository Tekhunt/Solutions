from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from clean_city.models.user_model import User


class TestDeactivateUser(APITestCase):
    def setUp(self):
        self.admin = User.objects.create(
            username='admin',
            password='admin@12345',
            email="admin@gmail.com",
            first_name="admin1",
            last_name="admin2",
            phone="123456789",
            is_staff=True,
            is_superuser=True,
            is_admin=True,
            )
        self.manager = User.objects.create(
            username='manager',
            password='manager@12345',
            email="manager@gmail.com",
            first_name="manager1",
            last_name="manager2",
            phone="123456789",
            is_staff=True,
            is_manager=True,
            is_superuser=False,
            is_admin=False,
            )
        self.cleaner = User.objects.create(
            username='cleaner',
            password='cleaner@12345',
            email="cleaner@gmail.com",
            first_name="cleaner1",
            last_name="cleaner2",
            phone="123456789",
            is_staff=True,
            is_cleaner=True,
        )

    def test_deactivate_user_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(reverse('deactivate-user', kwargs={'pk': self.manager.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(id=self.manager.id).is_active, False)

    def test_deactivate_user_cleaner(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(reverse('deactivate-user', kwargs={'pk': self.cleaner.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(id=self.cleaner.id).is_active, False)

    def test_delete_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(reverse('deactivate-user', kwargs={'pk': self.manager.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)