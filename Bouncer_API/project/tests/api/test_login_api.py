from django.urls import include, path, reverse
from django.test import TestCase
from db.models.user_model import User

class TestViews(TestCase):
    urlpatterns = [
        path('api/login', include('api.urls')),
    ]
    def setUp(self):
        self.url = 'login'
        self.user1 = User.objects.create(first_name='saheed', last_name='mosh', email='chizzy@gmail.com', phone_number='8067471928', password='private', otp_code='12345', email_verified=True)
    def test_view_url_at_wrong_location(self):
        response = self.client.get('login/')
        self.assertEqual(response.status_code, 404)
    def test_home_page_status_code(self):
        response= self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_about_page_status_code(self):
        response= self.client.get('/api/v1/verify-otp/')
        self.assertEquals(response.status_code, 404)
    def test_login_view_endpoint(self):
        response = self.client.get('/api/login/')
        self.assertNotEqual(response.status_code, 200)
    def test_view_url_at_wrong_endpoint(self):
        response= self.client.get('/api/v1/login/')
        self.assertNotEqual(response.status_code, 500)
        