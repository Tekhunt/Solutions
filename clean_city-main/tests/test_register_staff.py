from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from clean_city.models.user_model import User


class RegisterStaffTest(APITestCase):
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

        self.valid_payload = {
            "email": "test@gmail.com",
            "first_name": "test",
            "last_name": "user",
            "phone": "123456789",
            "city": "test_city",
            "user_type": "manager",

        }
        self.valid_username_manager = f"{self.valid_payload['first_name'].capitalize()} {self.valid_payload['last_name'].capitalize()}"

        self.valid_payload_cleaner = {
            "email": "test2@gmail.com",
            "first_name": "test2",
            "last_name": "user1",
            "phone": "123456789",
            "city": "test_city",
            "user_type": "cleaner",
        }
        self.valid_username_cleaner = f"{self.valid_payload_cleaner['first_name'].capitalize()} {self.valid_payload_cleaner['last_name'].capitalize()}"

        self.valid_payload_bin_collector = {
            "email": "test3@gmail.com",
            "first_name": "test3",
            "last_name": "user2",
            "phone": "123456589",
            "city": "test_city",
            "user_type": "garbage collector",
        }
        self.valid_username_bin_collector = f"{self.valid_payload_bin_collector['first_name'].capitalize()} {self.valid_payload_bin_collector['last_name'].capitalize()}"

        self.url = reverse('register_staff')
        

    def test_register_staff_manager_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_register_staff_manager_failure(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_register_staff_failure_email_exists(self):
        self.client.force_authenticate(user=self.admin)
        self.valid_payload['email'] = 'admin@gmail.com'
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_register_cleaner_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, self.valid_payload_cleaner, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.filter(is_cleaner=True).count(), 1)

    def test_register_cleaner_failure(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.filter(is_cleaner=True).count(), 0)
    
    def test_register_bin_collector_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, self.valid_payload_bin_collector, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.filter(is_bin_collector=True).count(), 1)

    def test_register_bin_collector_failure(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.filter(is_bin_collector=True).count(), 0)

    def test_valid_username_manager(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.filter(username=self.valid_username_manager).count(), 1)

    def test_valid_username_cleaner(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, self.valid_payload_cleaner, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.filter(username=self.valid_username_cleaner).count(), 1)

    def test_valid_username_bin_collector(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, self.valid_payload_bin_collector, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.filter(username=self.valid_username_bin_collector).count(), 1)

