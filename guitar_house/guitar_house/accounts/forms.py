from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model, authenticate
from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ValidationError

from guitar_house.accounts.models import GuitarHouseUser

UserModel = get_user_model()
class GuitarUserCreationForm(auth_forms.UserCreationForm):
    user = None
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


    def clean(self):
        email = self.cleaned_data.get('email')

        #
        # Perform custom validation
        if email and UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered. Please use a different email.")
        return self.cleaned_data




class GuitarUserChangeForm(auth_forms.UserChangeForm):
    pass


class GuitarUserLoginForm(auth_forms.AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('email','password')


    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')


        if email and password:
            self.user_cache = authenticate(username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid email or password")

        return self.cleaned_data
