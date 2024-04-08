from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from guitar_house.common.forms import ReplyForm
from guitar_house.common.models import Message
from guitar_house.guitar.models import Guitar

UserModel = get_user_model()

class ReplyMessageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = UserModel.objects.create_user(email='user1@example.com', password='password1')
        self.user2 = UserModel.objects.create_user(email='user2@example.com', password='password2')
        self.guitar = Guitar.objects.create(
            brand='Gibson',
            model='Les Paul',
            type='electric',
            price=1000.00,
            image_url='https://upload.wikimedia.org',
            description='Gibson Les Paul classic series electric guitar',
            short_description='Gibson Les Paul ',
            user=self.user2)
        self.message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            guitar=self.guitar,
            message='Test message')

    def test_reply_message_view_get(self):
        self.client.login(email='user1@example.com', password='password1')
        response = self.client.get(reverse('reply-message', kwargs={'message_id': self.message.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/reply-message.html')
        self.assertIsInstance(response.context['form'], ReplyForm)
        self.assertEqual(response.context['message'], self.message)

    def test_reply_message_view_post(self):
        self.client.login(email='user1@example.com', password='password1')
        response = self.client.post(reverse('reply-message', kwargs={'message_id': self.message.pk}), {'message': 'Reply'})
        self.assertRedirects(response, reverse('show-messages'))
        self.assertEqual(self.user1.received_messages.count(), 1)

    def test_invalid_form_submission(self):
        self.client.login(email='user1@example.com', password='password1')
        response = self.client.post(reverse('reply-message', kwargs={'message_id': self.message.pk}), {'message': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/reply-message.html')
        self.assertIsInstance(response.context['form'], ReplyForm)
        self.assertEqual(response.context['message'], self.message)
        self.assertEqual(self.user1.received_messages.count(), 0)


    #TODO: this test bot working
    def test_unauthenticated_user_redirected_to_login(self):
        response = self.client.get(reverse('reply-message', kwargs={'message_id': self.message.pk}))
        self.assertRedirects(response,reverse('sign-in'))
        response = self.client.post(reverse('reply-message', kwargs={'message_id': self.message.pk}), {'message': 'Reply'})
        self.assertRedirects(response,reverse('sign-in'))
        self.assertEqual(self.user1.received_messages.count(), 0)
