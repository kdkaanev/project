from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class RegisterUserViewTestCase(TestCase):

    def setUp(self):
        self.register_url = reverse('sign-up')
        self.user_data = {

            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

    def test_register_user_success(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserModel.objects.filter(email='test@example.com').exists())

    def test_register_user_fail(self):
        response = self.client.post(self.register_url, {})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(UserModel.objects.filter(email='test@example.com').exists())

    def test_register_user_invalid_form(self):
        invalid_user_data = {

            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(self.register_url, invalid_user_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(UserModel.objects.filter(email='test@example.com').exists())

    def test_register_user_existing_email(self):
        UserModel.objects.create_user(email='test@example.com', password='existingpassword')

        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UserModel.objects.filter(email='test@example.com').exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'warning')

        self.assertEqual(messages[0].message, "This email is already registered. Please use a different email.")


class SignInUserViewTestCase(TestCase):

    def setUp(self):
        self.signin_url = reverse('sign-in')
        self.user_data = {
            'username': 'test@example.com',
            'password': 'testpassword',
        }

        self.user = UserModel.objects.create_user(email='test@example.com', password='testpassword')

    def test_signin_user_invalid_credentials(self):
        invalid_user_data = {
            'username': 'testuser',
            'password': 'invalidpassword',
        }
        response = self.client.post(self.signin_url, invalid_user_data)
        self.assertEqual(response.status_code, 200)

    def test_signin_user_success(self):
        response = self.client.post(self.signin_url, self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_signin_user_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.signin_url, self.user_data)
        self.assertEqual(response.status_code, 200)


class EditProfileViewTestCase(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(email='test@example.com', password='testpassword')
        self.profile = self.user.profile

    def test_edit_profile_view(self):
        self.client.login(email='test@example.com', password='testpassword')
        url = reverse('edit-profile', kwargs={'pk': self.profile.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_profile_view_post(self):
        self.client.login(email='test@example.com', password='testpassword')
        url = reverse('edit-profile', kwargs={'pk': self.profile.pk})
        success_url = reverse('profile', kwargs={'pk': self.profile.pk})
        updated_data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'date_of_birth': '2000-01-01',
            'profile_picture': 'https://example.com/profile_picture.jpg',
            'phone_number': '1234567890',
        }
        date_of_birth_from_form = datetime.strptime(updated_data['date_of_birth'], '%Y-%m-%d').date()

        response = self.client.post(url, data=updated_data)
        self.assertRedirects(response, success_url)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.first_name, updated_data['first_name'])
        self.assertEqual(self.profile.last_name, updated_data['last_name'])
        self.assertEqual(self.profile.date_of_birth, date_of_birth_from_form)
        self.assertEqual(self.profile.profile_picture, updated_data['profile_picture'])
        self.assertEqual(self.profile.phone_number, updated_data['phone_number'])
