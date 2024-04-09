from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from guitar_house.guitar.models import Guitar, Review
from tests.create_guitar import _create_guitar

UserModel = get_user_model()


class ReviewGuitarsViewTest(TestCase):
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

    def test_review_guitars_view(self):
        response = self.client.get(reverse('guitar-reviews', kwargs={'pk': self.guitar.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'guitars/review.html')
        self.assertEqual(response.context['guitar'], self.guitar)
        self.assertQuerysetEqual(response.context['reviews'], Review.objects.none())

    def test_review_guitars_view_with_reviews(self):
        review1 = Review.objects.create(guitar=self.guitar, rating=4, text='Great guitar', user=self.user)
        review2 = Review.objects.create(guitar=self.guitar, rating=5, text='Amazing guitar', user=self.user)

        response = self.client.get(reverse('guitar-reviews', kwargs={'pk': self.guitar.pk}))
        self.assertQuerysetEqual(response.context['reviews'], Review.objects.all(), ordered=False)
        self.assertIn(review1, response.context['reviews'])
        self.assertIn(review2, response.context['reviews'])

    def test_review_guitars_view_invalid_guitar(self):
        response = self.client.get(reverse('guitar-reviews', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)
