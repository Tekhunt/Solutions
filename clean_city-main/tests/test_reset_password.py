from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from clean_city.models import User


class PasswordResetTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='testcase',
                                        email='testcase@example.com',
                                        phone='+2347067851436',
                                        otp='123456',
                                        profile_image='https://www.google.com/imgres?imgurl=https%3A%2F',
                                        password='Password01#'),

    def test_reset_password_correct_email(self):
        data = {
            "email": 'testcase@example.com'
        }
        response = self.client.post(reverse('forgot-password'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reset_password_wrong_email(self):
        data = {
            "email": 'randomemail@example.com'
        }
        response = self.client.post(reverse('forgot-password'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_correct_otp(self):
        email = 'testcase@example.com'
        data = {
            'otp_or_old_password': '123456',
            'new_password': 'Paasword01#_'
        }
        response = self.client.post(reverse('password-reset', args=[email]), data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_wrong_otp(self):
        email = 'testcase@example.com'
        data = {
            'otp_or_old_password': '789101',
            'new_password': 'password234%'
        }
        response = self.client.post(reverse('password-reset', args=[email]), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_old_password_as_otp(self):
        email = 'testcase@example.com'
        data = {
            'otp_or_old_password': 'Password01#',
            'new_password': 'password'
        }
        response = self.client.post(reverse('password-reset', args=[email]), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
