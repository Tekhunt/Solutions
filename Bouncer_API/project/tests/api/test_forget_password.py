
from django.urls import include, path, reverse
from django.test import TestCase


class TestViews(TestCase):
    urlpatterns = [
        path('api/auth/forgot_password/', include('api.urls')),
    ]

    def setUp(self):
        self.name = 'forgot-password'

    def test_view_url_at_wrong_location(self):
        response = self.client.get('api/account/forgot-password/')
        self.assertEqual(response.status_code, 404)

    def test_home_page_status_code(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.status_code, 200)

    def test_view_url_at_right_location(self):
        response = self.client.get('/api/v1/forgot_password/')
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_at_right_location_no_error(self):
        response = self.client.get('/api/auth/forgot_password/')
        self.assertNotEqual(response.status_code, 500)
