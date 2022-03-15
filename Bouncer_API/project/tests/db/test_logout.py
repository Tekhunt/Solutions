from django.urls import include, path, reverse
from django.test import TestCase



class TestViews(TestCase):

    urlpatterns = [
        path('api/auth/v1/', include('api.urls')),
        
    ]
    
    def setUp(self):
        self.name = 'logout'

    def test_view_url_at_wrong_location(self):
        response = self.client.get('api/auth/v1/logout/')
        print(response)
        self.assertEqual(response.status_code, 404)

    
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/api/auth/v1/logout/')
        self.assertEquals(response.status_code, 401)

    def test_view_url_at_right_location(self):
        response = self.client.get('/api/auth/v1/logout/')
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_at_right_location_no_error(self):
        response = self.client.get('/api/auth/v1/logout/')
        self.assertNotEqual(response.status_code, 500)

  

