from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from guitar_house.common.forms import MessageForm
from guitar_house.guitar.models import Guitar

UserModel = get_user_model()


class ContactSellerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='testuser@example.com', password='password')
        self.guitar = Guitar.objects.create(
            brand='Gibson',
            model='Les Paul',
            type='electric',
            price=1000.00,
            image_url='https://upload.wikimedia.org',
            description='Gibson Les Paul classic series electric guitar',
            short_description='Gibson Les Paul ',
            user=self.user)

    def test_authenticated_user_can_contact_seller(self):
        self.client.login(email='testuser@example.com', password='password')
        response = self.client.post(reverse('messages', kwargs={'guitar_id': self.guitar.pk}),
                                    {'message': 'Test message'})
        self.assertRedirects(response, reverse('guitar-info', kwargs={'pk': self.guitar.pk}))
        self.assertEqual(self.user.received_messages.count(), 1)

    def test_unauthenticated_user_redirected_to_login(self):
        response = self.client.get(reverse('messages', kwargs={'guitar_id': self.guitar.pk}))
        self.assertRedirects(response, reverse('sign-in'))

    def test_message_form_displayed_for_get_request(self):
        self.client.login(email='testuser@example.com', password='password')
        response = self.client.get(reverse('messages', kwargs={'guitar_id': self.guitar.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/contact_seller.html')
        self.assertIsInstance(response.context['form'], MessageForm)
        self.assertEqual(response.context['guitar'], self.guitar)

    def test_invalid_form_submission(self):
        self.client.login(email='testuser@example.com', password='password')
        response = self.client.post(reverse('messages', kwargs={'guitar_id': self.guitar.pk}), {'message': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/contact_seller.html')
        self.assertIsInstance(response.context['form'], MessageForm)
        self.assertEqual(response.context['guitar'], self.guitar)
        self.assertEqual(self.user.received_messages.count(), 0)

    def test_unauthenticated_user_redirected_to_login_on_post(self):
        response = self.client.post(reverse('messages', kwargs={'guitar_id': self.guitar.pk}),
                                    {'message': 'Test message'})
        self.assertRedirects(response, reverse("sign-in"))
        self.assertEqual(self.user.received_messages.count(), 0)
