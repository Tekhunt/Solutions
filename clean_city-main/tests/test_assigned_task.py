from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from clean_city.models import User, Task, CheckList, CleaningArea



class GetUserTaskViewTestCase(APITestCase):
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
        self.list_of_checklist = CheckList.objects.create(
            place = "test_place",
            list ={"test_list": "false", "test_list2": "false"}
        )
        self.cleaning_areas = CleaningArea.objects.create(
            name = "test_place",
            checklist ={"test_list": "false", "test_list2": "false"}
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
        self.valid_payload = {
            "title": "test",
            "description": "test 123",
            "location": "test_city",
            "task_status": "Pending",
            "created_by": self.admin.id,
            "assigned_to": self.cleaner.id,
            "start_date": "2022-09-04 06:00",
            "end_date": "2022-09-14 06:00",
            'checklist': [self.list_of_checklist.id],

        }
        
        self.url = reverse('get_task')
    def test_get_user_task_success(self):
        self.client.force_authenticate(user=self.cleaner)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)