from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from clean_city.models import User, Task, CheckList, CleaningArea


class AcceptTaskTest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create(
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
        self.cleaner = User.objects.create(
            username='cleaner',
            password='cleaner@12345',
            email="cleaner@gmail.com",
            first_name="cleaner1",
            last_name="cleaner2",
            phone="123456789",
            is_cleaner=True,
        )
        
        self.list_of_checklist = CheckList.objects.create(
            place = "test_place",
            list ={"test_list": "false", "test_list2": "false"}
        )
        self.cleaning_areas = CleaningArea.objects.create(
            name = "test_place",
            checklist ={"test_list": "false", "test_list2": "false"}
        )


        self.creat_task = Task.objects.create(
            title= "test",
            description= "test 123",
            location= "test_city",
            created_by= self.admin,
            start_date = "2022-09-04 06:00",
            end_date = "2022-09-14 06:00",

        )
        self.creat_task.assigned_to.add(self.cleaner)
        self.creat_task.cleaning_area.add(self.cleaning_areas)
        self.url = reverse('accept-task', kwargs={'id': self.creat_task.id, 'bool': 'true'})

    def test_accept_task_succesfully_accepted(self):
        self.client.force_authenticate(user=self.cleaner)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accept_task_succesfully_rejected(self):
        self.client.force_authenticate(user=self.cleaner)
        self.url = reverse('accept-task', kwargs={'id': self.creat_task.id, 'bool': 'false'})
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accept_task_with_invalid_url(self):
        self.client.force_authenticate(user=self.cleaner)
        self.url = reverse('accept-task', kwargs={'id': self.creat_task.id+1, 'bool': 'false'})
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_accept_task_without_authentication(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_accept_task_with_invalid_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
