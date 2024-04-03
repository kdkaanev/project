from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from guitar_house.accounts.models import GuitarHouseUser, Profile


# Create your tests here.

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
        self.assertTrue(GuitarHouseUser.objects.filter(email='test@example.com').exists())

    def test_register_user_fail(self):
        response = self.client.post(self.register_url, {})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(GuitarHouseUser.objects.filter(email='test@example.com').exists())

    def test_register_user_existing_email(self):
        GuitarHouseUser.objects.create_user(email='test@example.com', password='existingpassword')

        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(GuitarHouseUser.objects.filter(email='test@example.com').exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'warning')

        self.assertEqual(messages[0].message, "This email is already registered. Please use a different email.")

    def test_register_user_invalid_form(self):
        invalid_user_data = {

            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(self.register_url, invalid_user_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(GuitarHouseUser.objects.filter(email='test@example.com').exists())


class SignInUserViewTestCase(TestCase):

    def setUp(self):
        self.signin_url = reverse('sign-in')
        self.user_data = {
            'username': 'test@example.com',
            'password': 'testpassword',
        }

        self.user = GuitarHouseUser.objects.create_user(email='test@example.com', password='testpassword')

    def test_signin_user_success(self):
        response = self.client.post(self.signin_url, self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_signin_user_invalid_credentials(self):
        invalid_user_data = {
            'username': 'testuser',
            'password': 'invalidpassword',
        }
        response = self.client.post(self.signin_url, invalid_user_data)
        self.assertEqual(response.status_code, 200)

    def test_signin_user_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.signin_url, self.user_data)
        self.assertEqual(response.status_code, 200)


class DetailProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = GuitarHouseUser.objects.create_user(email='test@example.com', password='testpassword')

    def test_detail_profile_view(self):
        profile = self.user.profile
        url = reverse('profile', kwargs={'pk': profile.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, profile.full_name)

    def test_detail_profile_view_invalid_profile(self):
        url = reverse('profile', kwargs={'pk': 999})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)




class EditProfileViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = GuitarHouseUser.objects.create_user(email='test@example.com', password='testpassword')
        # Create a test profile associated with the user


    def test_edit_profile_view(self):
        profile = self.user.profile
        # Log in as the test user
        self.client.login(username='est@example.com', password='testpassword')
        # Get the URL for the edit profile view
        url = reverse('edit-profile', kwargs={'pk': profile.pk})
        # Make a GET request to the URL
        response = self.client.get(url)
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the profile data is present in the form
        self.assertContains(response, profile.first_name)
        self.assertContains(response, profile.last_name)

    def test_edit_profile_view_post(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')
        # Get the URL for the edit profile view
        url = reverse('edit-profile', kwargs={'pk': self.profile.pk})
        # Make a POST request to the URL with updated profile data
        updated_data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'date_of_birth': '2000-01-01',  # Provide updated values for other fields as needed
            # Add other fields as needed
        }
        response = self.client.post(url, data=updated_data)
        # Check that the form submission redirects to the success URL
        self.assertRedirects(response, reverse('profile', kwargs={'pk': self.profile.pk}))
        # Refresh the profile object from the database
        self.profile.refresh_from_db()
        # Check that the profile data has been updated
        self.assertEqual(self.profile.first_name, updated_data['first_name'])
        self.assertEqual(self.profile.last_name, updated_data['last_name'])
        # Add assertions for other updated fields as needed

