from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from clean_city.models import User, Task, CheckList, CleaningArea


class UpdateTaskTest(APITestCase):
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

        self.bin_collector = User.objects.create(
            username='bin_collector',
            password='bin_collector@12345',
            email="bin_collector@gmail.com",
            first_name="bin_collector1",
            last_name="bin_collector2",
            phone="123456789",
            is_bin_collector=True,
        )

        self.list_of_checklist = CheckList.objects.create(
            place = "test_place",
            list ={"test_list": "false", "test_list2": "false"}
        )
        self.cleaning_areas = CleaningArea.objects.create(
            name = "test_place",
            checklist ={"test_list": "false", "test_list2": "false"}
        )


        self.created_task = Task.objects.create(
            title="test",
            description="test 123",
            location="test_city",
            created_by=self.admin,
            start_date="2022-09-04 06:00",
            end_date="2022-09-14 06:00",
            task_status=Task.STATUS[0][0],
        )

        self.created_task.assigned_to.add(self.cleaner)
        self.created_task.cleaning_area.add(self.cleaning_areas)
        self.url = reverse('task-update', kwargs={'pk': self.created_task.id})

        self.valid_payload = {
            "task_status": Task.STATUS[0][0],
            "cleaning_area": [
                {
                    "id": self.list_of_checklist.id,
                    "place": self.list_of_checklist.place,
                    "list": self.list_of_checklist.list,
                }
            ],
        }
        self.valid_payload_for_cleaner = {
            "task_status": Task.STATUS[0][0],
            "checklist": [
                {
                    "id": self.list_of_checklist.id,
                    "place": self.list_of_checklist.place,
                    "list": self.list_of_checklist.list,
                }
            ],
        }


        self.valid_payload_for_admin = {
            "title": "test",
            "description": "test 12356",
            "location": "test_city 2",
            "start_date": "2022-09-04 06:00",
            "end_date": "2022-09-14 06:00",
            "task_status": Task.STATUS[0][0],
        }

        self.invalid_payload = {
            "cleaning_areas": "hello",}

    def test_update_task_with_valid_payload(self):
        self.client.force_authenticate(user=self.cleaner)
        response = self.client.put(self.url, self.valid_payload_for_cleaner, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task_with_valid_payload_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(self.url, self.valid_payload_for_admin, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_task_without_authentication(self):
        response = self.client.put(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_task_with_invalid_authentication(self):
        self.client.force_authenticate(user=self.bin_collector)
        response = self.client.put(self.url, self.valid_payload_for_cleaner, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_task_return_value_cleaner(self):
        self.client.force_authenticate(user=self.cleaner)
        response = self.client.put(self.url, self.valid_payload_for_cleaner, format='json')
        self.assertEqual(response.data['task_status'], self.valid_payload['task_status'])

    def test_update_task_return_value_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(self.url, self.valid_payload_for_admin, format='json')
        self.assertEqual(response.data['title'], self.valid_payload_for_admin['title'])
