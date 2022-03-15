from django.urls import reverse, path, include
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    urlpatterns = [
        path('password-reset/<otp>/', include('api.urls')),
    ]

    def setUp(self):
        self.name = 'password reset'

    def test_view_url_at_wrong_location(self):
        response = self.client.get('api/account/verify-otp/')
        self.assertEqual(response.status_code, 404)

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_code(self):
        response = self.client.get('/api/v1/login/')
        self.assertEquals(response.status_code, 404)

    def test_view_url_at_exact_location_reset_password(self):
        response = self.client.get('/api/v1/password-reset/<otp>/')
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_at_exact_location_token_check(self):
        response = self.client.get('/api/v1/password-reset/<uidb64>/<token>/')
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_at_exact_location_without_error_token_check(self):
        response = self.client.get(
            '/api/v1/register/password-reset/<uidb64>/<token>/')
        self.assertNotEqual(response.status_code, 500)

    def test_view_url_at_exact_location_without_error_reset(self):
        response = self.client.get('/api/v1/password-reset-complete')
        self.assertNotEqual(response.status_code, 500)
