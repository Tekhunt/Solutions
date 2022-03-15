from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from clean_city.models import User


class TestEditProfile(APITestCase):
    def setUp(self):
        self.sample_user = User.objects.create(
            username='admin',
            password='admin@12345',
            email="admin@cleancityllc.com",
            first_name="admin1",
            last_name="admin2",
            phone="123456789",
            is_staff=True,
            is_superuser=True,
            is_admin=True,
        )

        self.update_payload = {
        "username": "michaelDoe",
        "first_name": "michael",
        "last_name": "Doe",
        "email": "michael.Doe@clean.com",
        "phone": "07035834838",
        "city": "Lagos",
    }
        self.wrong_image_payload = {
        "profile_image": "wrong_image_format",
    }

        self.url = reverse('profile-update')

    def test_get_user_profile(self):
        self.client.force_authenticate(user=self.sample_user)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_profile_update_successful(self):
        self.client.force_authenticate(user=self.sample_user)
        response = self.client.put(
            self.url,  self.update_payload, format='json')       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'User data updated successfully')

    def test_user_profile_data_update(self):
        self.client.force_authenticate(user=self.sample_user)
        self.client.put(
            self.url,  self.update_payload, format='json')    
        get_update = User.objects.get(username='michaelDoe')
        self.assertEqual(get_update.first_name, self.update_payload.get('first_name'))
        self.assertNotEqual(get_update, None)

    def test_user_profile_update_wrong_image_format(self):
        self.client.force_authenticate(user=self.sample_user)
        res = self.client.put(
            self.url,   self.wrong_image_payload, format='json')  
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)  

    def tearDown(self) -> None:
        return super().tearDown()
