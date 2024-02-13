from rest_framework.test import APITestCase
from rest_framework import status
from .models import User_Details


class UserDetailsTestCase(APITestCase):

    def setUp(self):
        self.user1 = User_Details.objects.create(name='user1', email='user1@gmail.com', age=20)
        self.user2 = User_Details.objects.create(name='user2', email='user2@gmail.com', age=30)

    def test_user_list(self):
        url = '/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'user1')
        self.assertEqual(response.data[1]['name'], 'user2')

    def test_user_detail(self):
        url = f'/users/{self.user1.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'user1')

    def test_create_user(self):
        url = '/users/'
        data = {'name': 'user3', 'email': 'user3@example.com', 'age': 25}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User_Details.objects.count(), 3)
        self.assertEqual(User_Details.objects.get(pk=3).name, 'user3')

    def test_update_user(self):
        url = f'/users/{self.user1.pk}/'
        data = {'name': 'user1_updated', 'email': 'user1_updated@example.com','age': 21}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'user1_updated')

    def test_partial_update_user(self):
        url = f'/users/{self.user1.pk}/'
        data = {'name': 'user1_updated'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'user1_updated')

    def test_delete_user(self):
        url = f'/users/{self.user1.pk}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User_Details.objects.count(), 1)