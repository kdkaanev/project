from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms

from guitar_house.accounts.forms import GuitarUserCreationForm
from guitar_house.accounts.models import Profile
from guitar_house.guitar import models

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
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile.html'




def sign_out(request):
    logout(request)
    return redirect('index')


