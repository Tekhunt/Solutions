import token
from rest_framework import status
from rest_framework.reverse import reverse
from clean_city.models import User
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory



class TestGetCleanersAndBinCollectors(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.manager = User.objects.create(username='manager',
                                           email='manager@example.com',
                                           phone='+2347067851436',
                                           otp='123456',
                                           profile_image='https://www.google.com/imgres?imgurl=https%3A%2F',
                                           password='Password01#',
                                           is_manager=True)
        self.cleaner = User.objects.create(username='cleaner',
                                           email='cleaner@example.com',
                                           phone='+2345678979',
                                           otp='234567',
                                           profile_image='https://www.google.com/imgres?imgurl=https%3A%2F',
                                           password='password01#',
                                           is_cleaner=True)
        self.garbage = User.objects.create(username='garbage',
                                           email='garbage@example.com',
                                           phone='+2347067851436',
                                           otp='12345689',
                                           profile_image='https://www.google.com/imgres?imgurl=https%3A%2F',
                                           password='Password01#',
                                           is_bin_collector=True)
        self.admin = User.objects.create(username='admin',
                                         email='admin@example.com',
                                         phone='+23470678514378',
                                         otp='12345681',
                                         profile_image='https://www.google.com/imgres?imgurl=https%3A%2F',
                                         password='Password01#',
                                         is_admin=True)
                                        


    def test_get_cleaners_and_bin_collectors(self):
        url = reverse('get-cleaners-and-bin-collectors')
        request = self.factory.get(url, HTTP_AUTHORIZATION='Token {}'.format(token))
        user = User.objects.get(username='manager')
        force_authenticate(request, user=user)
        
