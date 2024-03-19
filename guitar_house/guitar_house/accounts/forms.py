from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()
class GuitarUserCreationForm(auth_forms.UserCreationForm):
    user = None
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)




class GuitarUserChangeForm(auth_forms.UserChangeForm):
    pass
