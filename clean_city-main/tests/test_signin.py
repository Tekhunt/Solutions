from django.urls import reverse
from clean_city.models.user_model import User
import base64
from rest_framework.test import APITestCase


class SigninTestCase(APITestCase):
    def setUp(self):
        password = str(base64.b64encode(b"password12345678"))
        self.user = User.objects.create(email="test@cleancityllc.com", 
                                       password=password )
    def test_signin(self):
        password = str(base64.b64encode(b"password12345678"))
        data = {
            "email":"test@cleancityllc.com",
            "password":password
        }
        self.assertEqual(data.get("password"), "b'cGFzc3dvcmQxMjM0NTY3OA=='")
