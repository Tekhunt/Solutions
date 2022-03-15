from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from clean_city.models import User, Task, CheckList, CleaningArea


class CreateTaskTest(APITestCase):
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

        self.valid_payload = {
            "title": "test",
            "description": "test 123",
            "location": "test_city",
            "created_by": self.admin.id,
            "assigned_to": [self.cleaner.id],
            "start_date": "2022-09-04 06:00",
            "end_date": "2022-09-14 06:00",
            'cleaning_areas': ["test_place"],

        }
        self.invalid_payload = {
            "title": "",
            "description": "",
            "location": "",
            "created_by": "",
            "assigned_to": "",
            "start_date": "2022-09-04 06:00",
            "end_date": "2022-09-14 06:00",
            'cleaning_areas': ["test_area"],
        }
        self.url = reverse('create-task')

    def test_create_task_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, self.valid_payload['title'])

    def test_create_task_invalid_payload(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(
            self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)
