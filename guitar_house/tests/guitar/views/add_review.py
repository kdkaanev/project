from django.contrib.auth import get_user_model

from guitar_house.guitar.forms import ReviewForm
from guitar_house.guitar.models import Review

from django.test import TestCase, Client
from django.urls import reverse

from tests.create_guitar import _create_guitar

UserModel = get_user_model()


class AddReviewViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test@example.com', password='password')
        self.guitar = _create_guitar(
            'Gibson',
            'Les Paul',
            'electric',
            1000.00,
            'https://upload.wikimedia.org',
            'Gibson Les Paul classic series electric guitar',
            'Gibson Les Paul ',
            self.user)

    def test_add_review_view_unauthenticated_user(self):
        response = self.client.get(reverse('add-review', kwargs={'guitar_id': self.guitar.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('guitar-reviews', kwargs={'pk': self.guitar.pk}))

    def test_add_review_view_authenticated_user_get(self):
        self.client.login(email='test@example.com', password='password')
        response = self.client.get(reverse('add-review', kwargs={'guitar_id': self.guitar.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'guitars/write-review.html')
        self.assertIsInstance(response.context['form'], ReviewForm)

    def test_add_review_view_authenticated_user_post(self):
        self.client.login(email='test@example.com', password='password')
        data = {'rating': 5, 'text': 'Excellent guitar'}
        response = self.client.post(reverse('add-review', kwargs={'guitar_id': self.guitar.pk}), data)
        self.assertRedirects(response, reverse('guitar-reviews', kwargs={'pk': self.guitar.pk}))
        self.assertTrue(Review.objects.filter(guitar=self.guitar, user=self.user, **data).exists())

    def test_add_review_view_invalid_form(self):
        self.client.login(email='test@example.com', password='password')
        data = {'rating': 6, 'text': 'Invalid guitar'}
        response = self.client.post(reverse('add-review', kwargs={'guitar_id': self.guitar.pk}), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Review.objects.filter(guitar=self.guitar, user=self.user, **data).exists())
