from django import forms
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from guitar_house.accounts.forms import GuitarUserCreationForm, GuitarUserLoginForm
from guitar_house.accounts.models import Profile

UserModel = get_user_model()
# Create your views here.
class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = GuitarUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


class SignInUserView(auth_views.LoginView):
    form_class = GuitarUserLoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile.html'


class EditProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'accounts/edit-profile.html'
    fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture', 'phone_number',)


    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

class DeleteProfileView(views.DeleteView):
    queryset = UserModel.objects.all()
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('index')



def sign_out(request):
    logout(request)
    return redirect('index')


