from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from guitar_house.guitar.models import Guitar

UserModel = get_user_model()


class CreateGuitarViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test@example.com', password='password')

    def test_create_guitar_view_get(self):
        self.client.login(email='test@example.com', password='password')
        response = self.client.get(reverse('guitar-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'guitars/add-guitar.html')
        self.assertContains(response, '<form')

    def test_create_guitar_view_post(self):
        self.client.login(email='test@example.com', password='password')
        data = {
            'brand': 'Fender',
            'model': 'Stratocaster',
            'type': 'Electric',
            'price': 1000,
            'image_url': 'https://example.com/image.jpg',
            'description': 'Description of the guitar',
            'short_description': 'Short description'
        }
        response = self.client.post(reverse('guitar-add'), data)
        self.assertRedirects(response, reverse('user-guitars'))
        self.assertTrue(Guitar.objects.filter(user=self.user, **data).exists())

    def test_unauthenticated_user_redirected_to_login(self):
        response = self.client.get(reverse('guitar-add'))
        self.assertRedirects(response, f'{reverse("sign-in")}?next={reverse("guitar-add")}')
        response = self.client.post(reverse('guitar-add'), {})
        self.assertRedirects(response, f'{reverse("sign-in")}?next={reverse("guitar-add")}')
        self.assertFalse(Guitar.objects.exists())
