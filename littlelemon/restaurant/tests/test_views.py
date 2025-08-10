from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class MenuTestView(TestCase):
  def setUp(self):
    User.objects.create_user('testuser', 'test@example.com', 'password')
    user = User.objects.get(username='testuser')
    self.client = APIClient()
    self.client.force_authenticate(user=user)
    Menu.objects.create(title="Ice Cream", price=80, inventory=100)
    self.url = reverse('menu-items')
  
  def test_get_all_menu_items(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response['Content-Type'], 'application/json')
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], 'Ice Cream')

class AuthTokenView(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='password123'
    )
    self.client= APIClient()
    self.url = reverse('api-auth')

  def test_successful_token_attainment(self):
    response = self.client.post(self.url, {
      'username' : 'testuser',
      'password' : 'password123',
    }, format='json')
    self.assertEqual(response.status_code, 200)


