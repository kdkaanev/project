from django import forms
from django.contrib import messages
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from guitar_house.accounts.forms import GuitarUserCreationForm, GuitarUserLoginForm
from guitar_house.accounts.models import Profile

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = GuitarUserCreationForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        email = form.cleaned_data.get('email')
        if email and UserModel.objects.filter(email=email).exists():
            messages.warning(
                self.request, "This email is already registered. Please use a different email."
            )
            return super().form_invalid(form)
        return super().form_invalid(form)

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


class EditProfileView(views.UpdateView, LoginRequiredMixin):
    queryset = Profile.objects.all()

    template_name = 'accounts/edit-profile.html'
    fields = (
        'first_name',
        'last_name',
        'date_of_birth',
        'profile_picture',
        'phone_number',
    )

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class DeleteProfileView(views.DeleteView, LoginRequiredMixin):
    queryset = UserModel.objects.all()
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('index')


def sign_out(request):
    logout(request)
    return redirect('index')
