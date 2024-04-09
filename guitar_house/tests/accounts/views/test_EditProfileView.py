from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class EditProfileViewTestCase(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(email='test@example.com', password='testpassword')
        self.profile = self.user.profile

    def test_edit_profile_view_get(self):
        self.client.login(email='test@example.com', password='testpassword')
        url = reverse('edit-profile', kwargs={'pk': self.profile.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/edit-profile.html')

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
        response = self.client.post(url, data=updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, success_url)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.first_name, updated_data['first_name'])
