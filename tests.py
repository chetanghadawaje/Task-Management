from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from tasks.models import Task

class TaskManagementAPITest(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_user_registration(self):
        response = self.client.post('/api/register/', {
            'username': 'newuser',
            'password': 'newpassword123'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_token_generation(self):
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {
            "title": "Complete project documentation",
            "description": "Finalize the project documentation",
            "due_date": "2024-11-10T15:30:00Z",
            "status": "Pending"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Complete project documentation")

    def test_get_tasks(self):
        Task.objects.create(
            user=self.user,
            title="Task 1",
            description="Test task",
            status="Pending"
        )
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_task(self):
        task = Task.objects.create(
            user=self.user,
            title="Task 2",
            description="Another test task",
            status="In Progress"
        )
        response = self.client.get(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Task 2")

    def test_update_task(self):
        task = Task.objects.create(
            user=self.user,
            title="Old Task",
            description="Old description",
            status="Pending"
        )
        response = self.client.put(f'/api/tasks/{task.id}/', {
            "title": "Updated Task",
            "description": "Updated description",
            "status": "Completed"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Task")
        self.assertEqual(response.data["status"], "Completed")

    def test_delete_task(self):
        task = Task.objects.create(
            user=self.user,
            title="Task to delete",
            status="Pending"
        )
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_unauthenticated_access(self):
        # Clear authentication to test unauthorized access
        self.client.credentials()
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)