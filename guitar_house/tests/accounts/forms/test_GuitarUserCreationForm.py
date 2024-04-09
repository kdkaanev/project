from django.contrib.auth import get_user_model
from django.test import TestCase

from guitar_house.accounts.forms import GuitarUserCreationForm

UserModel = get_user_model()


class TestGuitarUserCreationForm(TestCase):
    def test_clean_method_with_existing_email(self):
        existing_email = 'test@example.com'
        UserModel.objects.create_user(email=existing_email, password='password123')

        form_data = {
            'email': existing_email,
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }

        form = GuitarUserCreationForm(data=form_data)

        self.assertFalse(form.is_valid())

        self.assertEqual(form.errors['__all__'], ['This email is already registered. Please use a different email.'])
