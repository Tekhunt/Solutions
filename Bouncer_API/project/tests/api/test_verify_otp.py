
from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from api.views.verify_otp import Verify_otp_API
from db.models.user_model import User
from rest_framework import status

class VerifyOtpApiView(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(email= 'benardQgmail.com', password='myname@557', otp_code = 534756, email_verified= True)
        self.obj_verify = Verify_otp_API()
        return super().setUp()
    
    
        
    def test_otp_code(self):
        self.wrapper = self.user.otp_code
        self.assertEquals(self.wrapper, 534756)
        
    def test_email_verified(self):
        self.wrapper = self.user.email_verified 
        self.assertEquals(self.wrapper, True)
        
    
        
    def tearDown(self):
        return super().tearDown()
    