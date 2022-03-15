from django.urls import include, path
from django.test import TestCase


class TestViews(TestCase):
    urlpatterns = [
        path('api/v1/register', include('api.urls')),
    ]
    def setUp(self):
        self.name = 'register'

    def test_view_url_at_wrong_location(self):
        response = self.client.get('api/account/verify-otp/')
        self.assertEqual(response.status_code, 404)

    def test_home_page_status_code(self):
        response= self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # def test_about_page_status_code(self):
    #     response= self.client.get('/api/v1/verify-otp/')
    #     self.assertEquals(response.status_code, 405)

    def test_view_url_at_exact_location(self):
        response = self.client.get('/api/v1/register')
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_at_exact_location_without_error(self):
        response= self.client.get('/api/v1/register/')
        self.assertNotEqual(response.status_code, 500)
